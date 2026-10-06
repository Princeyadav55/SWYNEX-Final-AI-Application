import streamlit as st
import joblib

from intelligent_analyzer import analyze_message


# -----------------------------------------
# Load trained model
# -----------------------------------------

MODEL_PATH = "model/spam_classifier.pkl"

model = joblib.load(MODEL_PATH)


# -----------------------------------------
# Page configuration
# -----------------------------------------

st.set_page_config(
    page_title="Smart SMS Risk Analyzer",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------------------
# Custom styling
# -----------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 25px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------------------
# Header
# -----------------------------------------

st.markdown(
    '<div class="main-title">🤖 Smart SMS Risk Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Analyze an SMS message using Machine Learning and
    intelligent risk detection.
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------------------
# How it works
# -----------------------------------------

with st.expander("ℹ️ How does this application work?"):

    st.write(
        """
        1. Enter an SMS message.
        2. The Machine Learning model analyzes the text.
        3. The application predicts whether it is Spam or Not Spam.
        4. Suspicious indicators are detected.
        5. A risk level and safety recommendation are provided.
        """
    )


st.divider()


# -----------------------------------------
# Input section
# -----------------------------------------

st.subheader("📩 Enter Your SMS")

message = st.text_area(
    "SMS Message",
    placeholder=(
        "Example: Congratulations! You have won "
        "a free prize. Click now..."
    ),
    height=160
)


# -----------------------------------------
# Example messages
# -----------------------------------------

st.caption("💡 You can also try one of these examples:")

col1, col2 = st.columns(2)

with col1:

    if st.button("🚨 Try Spam Example"):

        message = (
            "Congratulations! You have won a free prize. "
            "Click the link now to claim your reward."
        )

with col2:

    if st.button("💬 Try Normal Example"):

        message = (
            "Hey, are you coming home today? "
            "Let me know when you reach."
        )


# -----------------------------------------
# Analyze button
# -----------------------------------------

if st.button(
    "🔍 Analyze SMS",
    use_container_width=True
):

    try:

        # ---------------------------------
        # Analyze message
        # ---------------------------------

        result = analyze_message(
            model,
            message
        )


        st.divider()

        st.subheader("📊 Analysis Result")


        # ---------------------------------
        # Main result
        # ---------------------------------

        if result["prediction"] == "spam":

            st.error("🚨 SPAM MESSAGE")

        else:

            st.success("✅ NOT SPAM")


        # ---------------------------------
        # Metrics
        # ---------------------------------

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Model Confidence",
                f"{result['confidence'] * 100:.2f}%"
            )


        with col2:

            st.metric(
                "Spam Probability",
                f"{result['spam_probability'] * 100:.2f}%"
            )


        with col3:

            st.metric(
                "Risk Level",
                result["risk_level"]
            )


        # ---------------------------------
        # Confidence progress
        # ---------------------------------

        st.subheader("🎯 Model Confidence")

        st.progress(
            result["confidence"]
        )


        # ---------------------------------
        # Risk level
        # ---------------------------------

        st.subheader("⚠️ Risk Assessment")


        if result["risk_level"] == "HIGH":

            st.error(
                "🔴 HIGH RISK — Be very careful with this message."
            )

        elif result["risk_level"] == "MEDIUM":

            st.warning(
                "🟠 MEDIUM RISK — Verify the message before taking action."
            )

        else:

            st.success(
                "🟢 LOW RISK — No major suspicious risk was detected."
            )


        # ---------------------------------
        # Suspicious indicators
        # ---------------------------------

        st.subheader("🔎 Detected Indicators")


        if result["indicators"]:

            for indicator in result["indicators"]:

                category = indicator["category"]

                keywords = ", ".join(
                    indicator["keywords"]
                )

                st.write(
                    f"• **{category.title()}**: "
                    f"{keywords}"
                )

        else:

            st.info(
                "No suspicious indicators detected."
            )


        # ---------------------------------
        # Recommendation
        # ---------------------------------

        st.subheader("💡 Safety Recommendation")

        st.info(
            result["recommendation"]
        )


        # ---------------------------------
        # Responsible AI note
        # ---------------------------------

        st.divider()

        st.caption(
            "⚠️ This AI prediction is not a guarantee. "
            "Always verify suspicious messages independently "
            "before clicking links or sharing personal information."
        )


    # -------------------------------------
    # Validation error
    # -------------------------------------

    except ValueError as e:

        st.warning(
            f"⚠️ {str(e)}"
        )


    # -------------------------------------
    # Unexpected error
    # -------------------------------------

    except Exception as e:

        st.error(
            "❌ Something went wrong while analyzing the message."
        )

        st.caption(
            f"Error type: {type(e).__name__}"
        )


# -----------------------------------------
# Footer
# -----------------------------------------

st.divider()

st.caption(
    "SWYNEX Technologies Internship — Task 4: Final AI Application"
)