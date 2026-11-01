#!/usr/bin/env python3
"""
AIGC Media Production Full Stack TCO Calculator 2026.
Combines ElevenLabs (Voice) + AdCreative.ai (Ad Visuals) + RunPod (GPU Inference).
"""
import argparse

def calculate(voice_chars, ad_credits, gpu_hours):
    # ElevenLabs Pro
    voice_base = 99.0
    voice_overage = (max(0, voice_chars - 500000) / 1000.0) * 0.24
    voice_total = voice_base + voice_overage

    # AdCreative Starter (10 credits) / Premium (100 credits = $189)
    ad_cost = 59.0 if ad_credits <= 10 else 189.0

    # RunPod RTX 4090 ($0.74/hr community/secure cloud)
    gpu_cost = gpu_hours * 0.74

    total = voice_total + ad_cost + gpu_cost

    print("=" * 65)
    print("AIGC Production Team Monthly Infrastructure Budget 2026")
    print("=" * 65)
    print(f"1. AI Voice (ElevenLabs Pro):           ${voice_total:.2f}/mo ({voice_chars:,} chars)")
    print(f"2. Ad Visuals (AdCreative.ai):          ${ad_cost:.2f}/mo ({ad_credits} credits)")
    print(f"3. Compute Infrastructure (RunPod GPU): ${gpu_cost:.2f}/mo ({gpu_hours}h @ $0.74/h)")
    print("-" * 65)
    print(f"Total Integrated Monthly Budget:        ${total:.2f}/mo")
    print("=" * 65)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AIGC Full Stack TCO Calculator")
    parser.add_argument("--voice-chars", type=int, default=500000)
    parser.add_argument("--ad-credits", type=int, default=10)
    parser.add_argument("--gpu-hours", type=int, default=200)
    args = parser.parse_args()
    calculate(args.voice_chars, args.ad_credits, args.gpu_hours)
