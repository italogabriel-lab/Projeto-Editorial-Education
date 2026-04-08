#!/usr/bin/env python3
"""
Diagnostic script for Gemini API configuration and quota status.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env from Projeto Bibline Academy
load_dotenv("Projeto Bibline Academy/.env")

def check_api_key():
    """Check if API key is configured."""
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ GEMINI_API_KEY not found")
        return None
    
    print(f"✅ API Key found: {api_key[:10]}...{api_key[-4:]}")
    return api_key

def test_api_connection(api_key):
    """Test basic API connectivity and quota status."""
    try:
        from google import genai
        from google.genai import types
        
        client = genai.Client(api_key=api_key)
        
        print("\n🔍 Testing API connection...")
        print("📡 Model: gemini-2.5-flash-preview-image")
        
        # Try a minimal request to check quota
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-image",
            contents="Test",
            config=types.GenerateContentConfig(
                response_modalities=["TEXT"],  # Text only to save quota
            ),
        )
        
        print("✅ API connection successful!")
        print(f"📝 Response: {response.text[:100]}...")
        return True
        
    except Exception as e:
        error_str = str(e)
        
        if "limit: 0" in error_str:
            print("\n❌ QUOTA EXHAUSTED - Free tier limit is ZERO")
            print("\n📊 This means:")
            print("   • Your Google Cloud project has NO quota allocated")
            print("   • Free tier is disabled for this project")
            print("   • You need to enable billing OR request quota increase")
        
        elif "API key not valid" in error_str:
            print("\n❌ Invalid API Key")
            print("   • Check if the key is correct")
            print("   • Try creating a new key at: https://aistudio.google.com/app/apikey")
        
        elif "API has not been used" in error_str:
            print("\n❌ Gemini API not enabled in your Google Cloud project")
            print("\n🔧 To fix:")
            print("   1. Go to: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com")
            print("   2. Select your project")
            print("   3. Click 'ENABLE'")
            print("   4. Wait 2-5 minutes")
            print("   5. Try again")
        
        else:
            print(f"\n❌ Error: {e}")
        
        return False

def check_google_cloud_setup(api_key):
    """Provide guidance on Google Cloud setup."""
    print("\n" + "="*80)
    print("📋 GOOGLE CLOUD CONSOLE CHECKLIST")
    print("="*80)
    
    print("\n1️⃣  Verify API is Enabled:")
    print("   → https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com")
    print("   Status: Must show 'ENABLED' (not 'ENABLE')")
    
    print("\n2️⃣  Check Quotas:")
    print("   → https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas")
    print("   Look for:")
    print("   • GenerateRequestsPerDayPerProjectPerModel-FreeTier")
    print("   • GenerateContentInputTokensPerModelPerMinute-FreeTier")
    print("   Current Status: limit: 0 (DISABLED)")
    
    print("\n3️⃣  Enable Billing (Recommended):")
    print("   → https://console.cloud.google.com/billing")
    print("   Benefits:")
    print("   • Increases quota from 0 to usable limits")
    print("   • Pay only for what you use beyond free tier")
    print("   • No minimum spend required")
    
    print("\n4️⃣  Create New API Key (If Needed):")
    print("   → https://aistudio.google.com/app/apikey")
    print("   • Delete current key")
    print("   • Create new key")
    print("   • Update in: Projeto Bibline Academy/.env")

def main():
    print("\n" + "="*80)
    print("🔍 GEMINI API DIAGNOSTIC TOOL")
    print("="*80 + "\n")
    
    # Step 1: Check API key
    print("Step 1: Checking API Key...")
    api_key = check_api_key()
    if not api_key:
        print("\n❌ Please add GEMINI_API_KEY to: Projeto Bibline Academy/.env")
        return 1
    
    # Step 2: Test connection
    print("\nStep 2: Testing API Connection...")
    success = test_api_connection(api_key)
    
    # Step 3: Provide guidance
    if not success:
        print("\nStep 3: Setup Guidance...")
        check_google_cloud_setup(api_key)
    
    print("\n" + "="*80)
    if success:
        print("✅ API is working! Ready to generate images.")
    else:
        print("⚠️  API has issues. Follow the checklist above to fix.")
    print("="*80 + "\n")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
