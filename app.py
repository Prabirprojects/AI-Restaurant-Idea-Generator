
import os
import json
import streamlit as st

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


# =========================================================
# STREAMLIT CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Restaurant Idea Generator",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ AI Restaurant Idea Generator")
st.caption("LangChain + OpenRouter powered restaurant concept generator")


# =========================================================
# PYDANTIC SCHEMAS
# =========================================================

class SignatureDish(BaseModel):
    name: str
    description: str
    estimated_price: str


class MenuItem(BaseModel):
    category: str
    item: str
    estimated_price: str


class RestaurantIdea(BaseModel):
    restaurant_name: str
    tagline: str
    concept: str
    target_audience: str
    ambience: str

    signature_dishes: list[SignatureDish] = Field(
        min_length=4,
        max_length=4
    )

    menu: list[MenuItem] = Field(
        min_length=8,
        max_length=8
    )

    pricing_strategy: str

    marketing_ideas: list[str] = Field(
        min_length=5,
        max_length=5
    )

    unique_selling_points: list[str] = Field(
        min_length=4,
        max_length=4
    )

    launch_plan: list[str] = Field(
        min_length=5,
        max_length=5
    )


# =========================================================
# MODEL
# =========================================================

def get_model():

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        st.error("OPENROUTER_API_KEY is missing in your .env file.")
        st.stop()

    model_name = os.getenv(
        "OPENROUTER_MODEL",
        "meta-llama/llama-3.1-8b-instruct"
    )

    return ChatOpenRouter(
        model=model_name,
        temperature=0.3,
        max_tokens=2500,
        max_retries=2,
        api_key=api_key
    )


# =========================================================
# PROMPT
# =========================================================

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert restaurant consultant.

Your ONLY task is to generate ONE restaurant idea.

IMPORTANT:
You MUST return data matching the provided RestaurantIdea schema.

DO NOT create any additional fields.

DO NOT add:
- appendix
- references
- financial projections
- competitor analysis
- management team
- risks
- demographics
- market trends
- location analysis
- extra sections
- extra menu items
- extra dishes

STRICT ARRAY LIMITS:

1. signature_dishes:
   EXACTLY 4 objects.

   Every object MUST contain:
   - name
   - description
   - estimated_price

2. menu:
   EXACTLY 8 objects.

   Every object MUST contain:
   - category
   - item
   - estimated_price

3. marketing_ideas:
   EXACTLY 5 strings.

4. unique_selling_points:
   EXACTLY 4 strings.

5. launch_plan:
   EXACTLY 5 strings.

The following top-level fields are REQUIRED:

- restaurant_name
- tagline
- concept
- target_audience
- ambience
- signature_dishes
- menu
- pricing_strategy
- marketing_ideas
- unique_selling_points
- launch_plan

Do not put marketing ideas, launch plan, menu items,
or business sections inside signature_dishes.

Keep all content concise and practical.

Do not write a business report.

Return ONLY the structured restaurant idea.
"""
    ),
    (
        "human",
        """
Create a restaurant idea using:

Cuisine: {cuisine}

Location: {location}

Budget: {budget}

Target Customers: {target}

Restaurant Theme: {theme}

Food Preferences: {preference}
"""
    )
])


# =========================================================
# GENERATE RESTAURANT IDEA
# =========================================================

def generate_restaurant_idea(
    cuisine,
    location,
    budget,
    target,
    theme,
    preference
):

    model = get_model()

    structured_model = model.with_structured_output(
        RestaurantIdea,
        method="json_schema"
    )

    chain = prompt | structured_model

    result = chain.invoke({
        "cuisine": cuisine,
        "location": location,
        "budget": budget,
        "target": target,
        "theme": theme,
        "preference": (
            ", ".join(preference)
            if preference
            else "No specific preference"
        )
    })

    # -----------------------------------------------------
    # EXTRA VALIDATION
    # -----------------------------------------------------

    if len(result.signature_dishes) != 4:
        raise ValueError(
            f"Expected 4 signature dishes, "
            f"got {len(result.signature_dishes)}"
        )

    if len(result.menu) != 8:
        raise ValueError(
            f"Expected 8 menu items, "
            f"got {len(result.menu)}"
        )

    if len(result.marketing_ideas) != 5:
        raise ValueError(
            f"Expected 5 marketing ideas, "
            f"got {len(result.marketing_ideas)}"
        )

    if len(result.unique_selling_points) != 4:
        raise ValueError(
            f"Expected 4 unique selling points, "
            f"got {len(result.unique_selling_points)}"
        )

    if len(result.launch_plan) != 5:
        raise ValueError(
            f"Expected 5 launch plan steps, "
            f"got {len(result.launch_plan)}"
        )

    return result.model_dump()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("🍴 Restaurant Details")

    cuisine = st.selectbox(
        "Cuisine",
        [
            "Indian",
            "Italian",
            "Chinese",
            "Mexican",
            "Japanese",
            "Korean",
            "American",
            "Mediterranean",
            "Thai",
            "Fusion",
            "Other"
        ]
    )

    location = st.text_input(
        "Location",
        placeholder="e.g. Bhubaneswar, India"
    )

    budget = st.selectbox(
        "Budget",
        [
            "Low",
            "Medium",
            "Premium"
        ]
    )

    target = st.text_input(
        "Target Customers",
        placeholder="e.g. College students"
    )

    theme = st.selectbox(
        "Restaurant Theme",
        [
            "Modern",
            "Traditional",
            "Minimalist",
            "Luxury",
            "Street Food",
            "Family Friendly",
            "Cafe",
            "Trendy / Instagrammable"
        ]
    )

    preference = st.multiselect(
        "Food Preferences",
        [
            "Vegetarian",
            "Vegan",
            "Non-Vegetarian",
            "Healthy",
            "Spicy",
            "Gluten-Free",
            "Desserts"
        ]
    )

    generate = st.button(
        "✨ Generate Restaurant Idea",
        type="primary",
        use_container_width=True
    )


# =========================================================
# MAIN APPLICATION
# =========================================================

if generate:

    with st.spinner("🤖 Generating your restaurant idea..."):

        try:

            data = generate_restaurant_idea(
                cuisine=cuisine,
                location=location or "Not specified",
                budget=budget,
                target=target or "General customers",
                theme=theme,
                preference=preference
            )

            st.success(
                "Restaurant idea generated successfully!"
            )

            # =================================================
            # RESTAURANT HEADER
            # =================================================

            st.header(
                f"🍽️ {data['restaurant_name']}"
            )

            st.subheader(
                f"“{data['tagline']}”"
            )

            st.write(
                data["concept"]
            )

            # =================================================
            # BASIC INFORMATION
            # =================================================

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Cuisine",
                    cuisine
                )

            with c2:
                st.metric(
                    "Budget",
                    budget
                )

            with c3:
                st.metric(
                    "Theme",
                    theme
                )

            st.divider()

            # =================================================
            # TARGET AUDIENCE & AMBIENCE
            # =================================================

            left, right = st.columns(2)

            with left:

                st.subheader(
                    "🎯 Target Audience"
                )

                st.write(
                    data["target_audience"]
                )

                st.subheader(
                    "🏠 Ambience"
                )

                st.write(
                    data["ambience"]
                )

                st.subheader(
                    "💎 Unique Selling Points"
                )

                for point in data["unique_selling_points"]:
                    st.write(
                        f"• {point}"
                    )

            with right:

                st.subheader(
                    "💰 Pricing Strategy"
                )

                st.write(
                    data["pricing_strategy"]
                )

                st.subheader(
                    "📣 Marketing Ideas"
                )

                for idea in data["marketing_ideas"]:
                    st.write(
                        f"• {idea}"
                    )

            st.divider()

            # =================================================
            # SIGNATURE DISHES
            # =================================================

            st.subheader(
                "⭐ Signature Dishes"
            )

            for dish in data["signature_dishes"]:

                with st.container(border=True):

                    st.markdown(
                        f"### {dish['name']}"
                    )

                    st.write(
                        dish["description"]
                    )

                    st.write(
                        f"**Estimated Price:** "
                        f"{dish['estimated_price']}"
                    )

            # =================================================
            # SAMPLE MENU
            # =================================================

            st.subheader(
                "📋 Sample Menu"
            )

            st.dataframe(
                data["menu"],
                use_container_width=True,
                hide_index=True
            )

            # =================================================
            # LAUNCH PLAN
            # =================================================

            st.subheader(
                "🚀 Launch Plan"
            )

            for index, step in enumerate(
                data["launch_plan"],
                start=1
            ):

                st.write(
                    f"**{index}.** {step}"
                )

            # =================================================
            # DOWNLOAD JSON
            # =================================================

            st.divider()

            st.download_button(
                label="⬇️ Download Restaurant Idea",
                data=json.dumps(
                    data,
                    indent=2,
                    ensure_ascii=False
                ),
                file_name="restaurant_idea.json",
                mime="application/json"
            )

        except Exception as e:

            st.error(
                "Something went wrong while generating "
                "the restaurant idea."
            )

            with st.expander(
                "Technical error"
            ):

                st.code(
                    str(e)
                )

            st.info(
                "If the error mentions json_schema or "
                "structured output, try a model that "
                "supports structured JSON output."
            )

else:

    st.info(
        "👈 Enter your restaurant requirements in the "
        "sidebar and click **Generate Restaurant Idea**."
    )

