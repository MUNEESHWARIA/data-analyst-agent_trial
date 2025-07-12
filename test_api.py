#!/usr/bin/env python3
"""
Test script for the Data Analyst Agent API
"""

import requests
import json
import base64
from PIL import Image
import io

def test_wikipedia_analysis():
    """Test Wikipedia movie analysis"""
    print("Testing Wikipedia Movie Analysis...")
    
    task = """
    Scrape the list of highest grossing films from Wikipedia. It is at the URL:
    https://en.wikipedia.org/wiki/List_of_highest-grossing_films

    Answer the following questions and respond with a JSON array of strings containing the answer.

    1. How many $2 bn movies were released before 2020?
    2. Which is the earliest film that grossed over $1.5 bn?
    3. What's the correlation between the Rank and Peak?
    4. Draw a scatterplot of Rank and Peak along with a dotted red regression line through it.
       Return as a base-64 encoded data URI, `"data:image/png;base64,iVBORw0KG..."` under 100,000 bytes.
    """
    
    # Test locally (update URL when deployed)
    url = "http://localhost:5000/api/"
    
    try:
        response = requests.post(url, data=task, headers={'Content-Type': 'text/plain'})
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Wikipedia Analysis Response:")
            print(f"   Question 1: {result[0]}")
            print(f"   Question 2: {result[1]}")
            print(f"   Question 3: {result[2]}")
            print(f"   Question 4: Plot generated (length: {len(result[3])} chars)")
            
            # Validate the plot
            if result[3].startswith("data:image/"):
                print("   ✅ Valid image data URI")
                
                # Optionally save the plot to verify
                try:
                    image_data = result[3].split(',')[1]
                    image_bytes = base64.b64decode(image_data)
                    image = Image.open(io.BytesIO(image_bytes))
                    image.save("test_plot.png")
                    print("   ✅ Plot saved as test_plot.png")
                except:
                    print("   ⚠️  Could not save plot image")
            else:
                print("   ❌ Invalid image format")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - make sure the server is running")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_court_analysis():
    """Test Indian court data analysis"""
    print("\nTesting Indian Court Data Analysis...")
    
    task = """
    The Indian high court judgement dataset contains judgements from the Indian High Courts.
    
    Answer the following questions and respond with a JSON object containing the answer.

    {
      "Which high court disposed the most cases from 2019 - 2022?": "...",
      "What's the regression slope of the date_of_registration - decision_date by year in the court=33_10?": "...",
      "Plot the year and # of days of delay from the above question as a scatterplot with a regression line. Encode as a base64 data URI under 100,000 characters": "data:image/webp:base64,..."
    }
    """
    
    url = "http://localhost:5000/api/"
    
    try:
        response = requests.post(url, data=task, headers={'Content-Type': 'text/plain'})
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Court Analysis Response:")
            for key, value in result.items():
                if key.startswith("Plot"):
                    print(f"   {key[:50]}...: Plot generated (length: {len(str(value))} chars)")
                else:
                    print(f"   {key}: {value}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - make sure the server is running")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_health_endpoint():
    """Test health check endpoint"""
    print("\nTesting Health Endpoint...")
    
    url = "http://localhost:5000/health"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Health Check Response:")
            print(f"   Status: {result.get('status')}")
            print(f"   Message: {result.get('message')}")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - make sure the server is running")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_home_endpoint():
    """Test home endpoint"""
    print("\nTesting Home Endpoint...")
    
    url = "http://localhost:5000/"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Home Endpoint Response:")
            print(f"   Message: {result.get('message')}")
            print(f"   Version: {result.get('version')}")
            print(f"   Endpoints: {result.get('endpoints')}")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - make sure the server is running")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_with_file():
    """Test API with file upload"""
    print("\nTesting File Upload...")
    
    # Create a test file
    with open("test_question.txt", "w") as f:
        f.write("""
        Scrape the list of highest grossing films from Wikipedia. It is at the URL:
        https://en.wikipedia.org/wiki/List_of_highest-grossing_films

        Answer the following questions and respond with a JSON array of strings containing the answer.

        1. How many $2 bn movies were released before 2020?
        2. Which is the earliest film that grossed over $1.5 bn?
        3. What's the correlation between the Rank and Peak?
        4. Draw a scatterplot of Rank and Peak along with a dotted red regression line through it.
        """)
    
    url = "http://localhost:5000/api/"
    
    try:
        with open("test_question.txt", "rb") as f:
            files = {"file": f}
            response = requests.post(url, files=files)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ File Upload Test:")
            print(f"   Response type: {type(result)}")
            print(f"   Response length: {len(result) if isinstance(result, list) else 'N/A'}")
            
            if isinstance(result, list) and len(result) >= 4:
                print(f"   ✅ All 4 answers received")
            else:
                print(f"   ⚠️  Unexpected response format")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run all tests"""
    print("=" * 60)
    print("DATA ANALYST AGENT API TESTING")
    print("=" * 60)
    
    # Test all endpoints
    test_health_endpoint()
    test_home_endpoint()
    test_wikipedia_analysis()
    test_court_analysis()
    test_with_file()
    
    print("\n" + "=" * 60)
    print("TESTING COMPLETE")
    print("=" * 60)
    print("\nNext steps:")
    print("1. If tests pass locally, deploy to your chosen platform")
    print("2. Update the URLs in this script to test the deployed version")
    print("3. Submit your GitHub repo URL and API endpoint URL")

if __name__ == "__main__":
    main()