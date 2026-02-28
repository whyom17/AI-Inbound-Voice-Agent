import asyncio, base64, os, time, certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
from sarvamai import AsyncSarvamAI
from sarvamai.types import AudioOutput, EventResponse

async def test():
    client = AsyncSarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])
    start = time.time()
    first_chunk = None

    async with client.text_to_speech_streaming.connect(model="bulbul:v3") as ws:
        await ws.configure(
            target_language_code="hi-IN",
            speaker="kavya",
            pace=1.1,
            min_buffer_size=50,
            output_audio_codec="pcm",
        )
        await ws.convert("नमस्ते! मैं आपकी कैसे सहायता कर सकती हूं?")
        await ws.flush()

        chunks = 0
        async for msg in ws:
            if isinstance(msg, AudioOutput):
                chunks += 1
                if chunks == 1:
                    first_chunk = time.time()
                    print(f"✅ First chunk arrived in {(first_chunk - start)*1000:.0f}ms")
            elif isinstance(msg, EventResponse):
                if msg.data.event_type == "final":
                    print(f"✅ Stream complete. {chunks} chunks in {(time.time()-start)*1000:.0f}ms total")
                    break

asyncio.run(test())
