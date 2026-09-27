import streamlit as st
from groq import Groq

# Page layout configuration
st.set_page_config(
    page_title="The Revenue Driver - Multi-Agent Growth Swarm",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ The Revenue Driver: Multi-Agent AI Growth Swarm")
st.write("Deploy a specialized swarm of 3 AI agents to analyze competitors, draft high-converting Meta ads, and map out email funnels.")

# Sidebar for Groq API Key
with st.sidebar:
    st.header("🔑 API Configuration")
    groq_api_key = st.secrets.get("GROQ_API_KEY") or st.text_input("Enter Groq API Key:", type="password")
    st.markdown("---")
    st.markdown("**Agent Swarm Roster:**")
    st.markdown("1. 🔍 **Agent 1:** SEO & Competitor Analyst")
    st.markdown("2. 📣 **Agent 2:** Direct-Response Copywriter")
    st.markdown("3. ✉️ **Agent 3:** Lifecycle Email Strategist")

# Business input fields
col1, col2 = st.columns(2)
with col1:
    product_url = st.text_input("Product URL / Website", placeholder="e.g., https://mybrand.com/product")
with col2:
    target_audience = st.text_input("Target Audience", placeholder="e.g., Busy remote software engineers aged 25-40")

# Swarm Execution Trigger
if st.button("🚀 Launch Growth Swarm", type="primary"):
    if not groq_api_key:
        st.error("Please enter your Groq API Key in the sidebar (or configure st.secrets) to proceed.")
    elif not product_url or not target_audience:
        st.warning("Please provide both a Product URL and Target Audience.")
    else:
        try:
            client = Groq(api_key=groq_api_key)
            model_name = "openai/gpt-oss-120b"

            # -------------------------------------------------------------
            # AGENT 1: Competitor & SEO Analyst
            # -------------------------------------------------------------
            st.markdown("---")
            st.subheader("🔍 Agent 1: Competitor & SEO Analysis")
            
            agent1_prompt = f"""
            You are Agent 1, a Senior SEO and Competitor Analyst.
            Analyze the following product link and target demographic:
            - Product URL: {product_url}
            - Target Audience: {target_audience}

            Tasks:
            1. Identify 3 likely competitor SEO key strategies for this product category.
            2. Extract 5 high-intent organic keywords to target.
            3. Outline a brief search-intent content gap analysis.
            """

            with st.spinner("Agent 1 is analyzing competitor strategies..."):
                res1 = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a world-class SEO analyst."},
                        {"role": "user", "content": agent1_prompt}
                    ],
                    model=model_name,
                    temperature=0.6,
                )
                agent1_output = res1.choices[0].message.content
                st.markdown(agent1_output)

            # -------------------------------------------------------------
            # AGENT 2: Meta Ad Copywriter (Feeds on Agent 1 Insights)
            # -------------------------------------------------------------
            st.subheader("📣 Agent 2: Hyper-Targeted Meta Ad Variations")
            
            agent2_prompt = f"""
            You are Agent 2, a Direct-Response Copywriter specializing in Meta Ads.
            Based on the audience ({target_audience}) and the SEO insights from Agent 1 below:
            
            --- Agent 1 Output ---
            {agent1_output}
            ----------------------

            Tasks:
            Write 5 distinct Meta Ad variations (Headline, Primary Text, Call To Action).
            - Variation 1: Pain-point focused
            - Variation 2: Social proof / Outcome focused
            - Variation 3: Curiosity / Feature hook
            - Variation 4: Direct offer / Urgency
            - Variation 5: Storytelling angle
            """

            with st.spinner("Agent 2 is crafting high-converting Meta ad variations..."):
                res2 = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are an elite Meta Ads performance copywriter."},
                        {"role": "user", "content": agent2_prompt}
                    ],
                    model=model_name,
                    temperature=0.7,
                )
                agent2_output = res2.choices[0].message.content
                st.markdown(agent2_output)

            # -------------------------------------------------------------
            # AGENT 3: Email Marketing Strategist (Synthesizes Full Strategy)
            # -------------------------------------------------------------
            st.subheader("✉️ Agent 3: 30-Day Lifecycle Email Funnel")
            
            agent3_prompt = f"""
            You are Agent 3, a Lifecycle & Email Marketing Strategist.
            Using the Product URL ({product_url}), Target Audience ({target_audience}), and ad messaging angles created by Agent 2:

            --- Agent 2 Output ---
            {agent2_output}
            ----------------------

            Tasks:
            Map out a 30-day lifecycle email marketing sequence containing 4 core touchpoints:
            1. Email 1 (Day 1): Welcome & High-Value Hook
            2. Email 2 (Day 4): Problem Amplification & Solution Bridge
            3. Email 3 (Day 10): Case Study / Customer Proof
            4. Email 4 (Day 20): Soft Pitch & Limited Incentive

            For each email, provide: Subject Line, Core Objective, and Content Brief/Outline.
            """

            with st.spinner("Agent 3 is constructing the 30-day email funnel..."):
                res3 = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are an expert retention and email marketing strategist."},
                        {"role": "user", "content": agent3_prompt}
                    ],
                    model=model_name,
                    temperature=0.7,
                )
                agent3_output = res3.choices[0].message.content
                st.markdown(agent3_output)

            st.success("✅ Multi-Agent Swarm execution complete!")

        except Exception as e:
            st.error(f"An error occurred during swarm execution: {str(e)}")
