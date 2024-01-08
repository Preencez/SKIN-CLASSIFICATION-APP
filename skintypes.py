import pandas as pd
import random

def generate_skin_data(num_examples):
    labels = list(range(1, num_examples + 1))
    skin_types = ["Oily Skin", "Dry Skin", "Normal Skin", "Combination Skin", "Sensitive Skin"]
    
    data = []
    for label in labels:
        skin_type = random.choice(skin_types)
        characteristics = ""
        recommendations = ""
        soap_recommendation = ""
        cream_recommendation = ""
        scrub_recommendation = ""
        face_cleanser_recommendation = ""
        face_cream_recommendation = ""
        Common_Skin_Concerns = ""

        if skin_type == "Oily Skin":
            characteristics = "Excess sebum, shiny appearance - Prone to enlarged pores, acne blemishes, blackheads, and whiteheads"
            recommendations = "Use a gentle, foaming cleanser with salicylic acid - Choose lightweight, oil-free, and non-comedogenic moisturizer with hyaluronic acid - Nourish and hydrate without clogging pores"
            soap_recommendation = "Oil-free and non-comedogenic cleanser"
            cream_recommendation = "Gel-based or water-based moisturizer"
            scrub_recommendation = "Exfoliating scrub with salicylic acid"
            face_cleanser_recommendation = "Foaming face cleanser"
            face_cream_recommendation = "Oil-free face cream"
            Common_Skin_Concerns = "Prone to acne breakouts and enlarged pores. May require extra care in managing oiliness."

        elif skin_type == "Dry Skin":
            characteristics = "Produces fewer natural oils - Dull, rough, or scaly appearance - Feels tight, less elastic - Prone to visible fine lines"
            recommendations = "Include gentle, soothing, and hydrating ingredients like glycerin - Use products with ceramides - Avoid long, hot showers - Moisturize multiple times per day - Choose fragrance-free, non-comedogenic, and alcohol-free skincare products"
            soap_recommendation = "Mild and hydrating cleanser"
            cream_recommendation = "Rich and creamy moisturizer"
            scrub_recommendation = "Hydrating scrub with moisturizing beads"
            face_cleanser_recommendation = "Hydrating face cleanser"
            face_cream_recommendation = "Night repair cream"
            Common_Skin_Concerns = "Prone to dryness, flakiness, and visible fine lines."

        elif skin_type == "Normal Skin":
            characteristics = "Balanced, not too dry nor too oily - Small pores, smooth texture - Not prone to breakouts, flakiness, or tightness"
            recommendations = "Maintain hydration with proper skincare - Lock in moisture with products containing aloe vera - Support the protective barrier"
            soap_recommendation = "Gentle and pH-balanced cleanser"
            cream_recommendation = "Any light and non-comedogenic moisturizer"
            scrub_recommendation = "Mild exfoliating scrub"
            face_cleanser_recommendation = "Everyday face cleanser"
            face_cream_recommendation = "Hydrating day cream"
            Common_Skin_Concerns = "Generally balanced, but may experience occasional sensitivity."

        elif skin_type == "Combination Skin":
            characteristics = "Areas that are both dry and oily - Oily T-zone, normal or dry cheeks - Variability based on seasons, stress, or hormone fluctuations"
            recommendations = "Focus on effective cleansing and hydration - Adapt skincare routine to address different areas - Use a combination of products suitable for both dry and oily skin"
            soap_recommendation = "Mild cleanser for combination skin"
            cream_recommendation = "Use separate moisturizers for dry and oily areas"
            scrub_recommendation = "Balancing scrub for combination skin"
            face_cleanser_recommendation = "Balancing face cleanser"
            face_cream_recommendation = "Dual-action face cream"
            Common_Skin_Concerns = "May experience both dryness and oiliness, especially in different facial areas."

        elif skin_type == "Sensitive Skin":
            characteristics = "Prone to redness, burning, itching, or dryness. Reactive to external irritants and certain ingredients."
            recommendations = "Identify triggers and avoid specific ingredients like fragrances and harsh chemicals - Modify environment to reduce exposure to triggering agents"
            soap_recommendation = "Hypoallergenic and fragrance-free cleanser"
            cream_recommendation = "Fragrance-free and gentle moisturizer"
            face_cleanser_recommendation = "Gentle face cleanser for sensitive skin"
            face_cream_recommendation = "Soothing face cream"
            scrub_recommendation = "Gentle exfoliating scrub for sensitive skin"
            Common_Skin_Concerns = "May experience heightened reactivity, leading to discomfort and visible reactions."

        data.append([label, skin_type, characteristics, recommendations, soap_recommendation, cream_recommendation, scrub_recommendation, face_cleanser_recommendation, face_cream_recommendation, Common_Skin_Concerns])

    df = pd.DataFrame(data, columns=["Label", "Skin Type", "Characteristics", "Skincare Recommendations", "Soap Recommendation", "Cream Recommendation", "Scrub Recommendation", "Face Cleanser Recommendation", "Face Cream Recommendation", "Common Skin Concerns"])
    return df

# Generate a dataset with a thousand examples
dataset = generate_skin_data(10000)

# Save the dataset to a CSV file
dataset.to_csv("skin_dataset.csv"),
