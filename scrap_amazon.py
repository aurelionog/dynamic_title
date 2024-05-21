import os
import openai
import dotenv
import json

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 


def generate_product_description(product_details, demographic_info):
    

    # Formatting product details for the prompt
    product_details_formatted = f"Title: {product_details['title']}\nDescription: {product_details['description']}"
    
    prompt = f"Create a compelling product title and description for the following product, " \
             f"tailored to the demographic group described. \n\n" \
             f"Product Details: \n{product_details_formatted}\n\n" \
             f"Demographic Information: \n{demographic_info}\n\n" \
             f"Output as JSON Title, SEO Metadata, Description: \n"


    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        )       
    output = response.choices[0].message.content.strip()

    try:
        # Attempt to convert output into a JSON object
        output_json = json.loads(output)
        title = output_json.get("Title", "No title generated")
        description = output_json.get("Description", "No description generated")
        seo_metadata = output_json.get("SEO Metadata", "No metadata generated")
    except json.JSONDecodeError:
        # If JSON parsing fails, display the raw output
        title = "Failed to parse output"
        description = output
        seo_metadata = ""

    return title, description, seo_metadata

# # Example usage:
# product_details = {
#     "title": "Samsung 27” Curved Monitor",
#     "description": "ultra-slim design, 1800R curvature, AMD FreeSync, 4ms response time, Eye Saver Mode."
# }
# demographic_info = "Retired lady from New Jersey who enjoys watching movies and online shopping."

# title_and_description = generate_product_description(api_key, product_details, demographic_info)
# print(title_and_description)
