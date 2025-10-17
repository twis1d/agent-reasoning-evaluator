import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Agent Reasoning Evaluator", page_icon="🤖", layout="wide")

st.title("🤖 Agent Reasoning Evaluator Dashboard")
st.write("Upload an `agent_data.json` file to evaluate agent reasoning paths and visualize the results.")

# Upload JSON file
uploaded_file = st.file_uploader("Upload your agent_data.json", type=["json"])

if uploaded_file is not None:
    try:
        data = json.load(uploaded_file)
        if not isinstance(data, list):
            st.error("JSON must be a list of objects.")
        else:
            # Evaluate data
            results = []
            for d in data:
                out = d.get("output", "").strip().lower()
                exp = (d.get("expected_output") or "").strip().lower()
                if exp:
                    is_correct = out == exp
                    error_type = "None" if is_correct else "Incorrect factual/logic error"
                else:
                    reasoning = d.get("reasoning", [])
                    is_correct = len(reasoning) >= 2
                    error_type = "Possible omission" if not is_correct else "None"

                results.append({
                    "Task": d.get("task"),
                    "Output": d.get("output"),
                    "Expected": d.get("expected_output"),
                    "Correct": is_correct,
                    "Error Type": error_type
                })

            df = pd.DataFrame(results)

            # Display table
            st.subheader("Evaluation Results")
            st.dataframe(df, use_container_width=True)

            # Metrics
            total = len(df)
            correct = df["Correct"].sum()
            incorrect = total - correct
            st.metric("✅ Correct", correct)
            st.metric("❌ Incorrect", incorrect)
            st.metric("📊 Accuracy (%)", round((correct / total) * 100, 2))

            # Chart
            st.subheader("Error Type Distribution")
            error_counts = df["Error Type"].value_counts()
            st.bar_chart(error_counts)

            # Option to download annotated data
            annotated_json = df.to_json(orient="records", indent=2)
            st.download_button(
                label="Download Annotated JSON",
                data=annotated_json,
                file_name="annotations.json",
                mime="application/json"
            )
    except Exception as e:
        st.error(f"Error loading JSON: {e}")
else:
    st.info("👆 Upload a JSON file above to get started.")
