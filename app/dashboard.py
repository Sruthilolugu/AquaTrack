import matplotlib.pyplot as plt
import streamlit as st

def plot_groundwater_levels(data, label, value_col):
    if not data.empty:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(data["Date"], data[value_col], marker="o", color="#1f77b4", label=label)
        ax.set_facecolor("#ffffff")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.set_xlabel("Date", color="#000000")
        ax.set_ylabel("Depth to Water Level (m)", color="#000000")
        ax.legend()
        plt.xticks(rotation=45, color="#000000")
        plt.yticks(color="#000000")
        st.pyplot(fig)
    else:
        st.warning(f"No data available for {label}.")

def show_summary(data, label, value_col):
    st.markdown(
        f"**Summary ({label}):**\n"
        f"- Average Depth to Water Level: {data[value_col].mean():.2f} m\n"
        f"- Minimum Depth to Water Level: {data[value_col].min():.2f} m\n"
        f"- Maximum Depth to Water Level: {data[value_col].max():.2f} m"
    )

def plot_recharge(data, label, value_col):
    recharge_data = data.sort_values("Date").copy()
    recharge_data["Recharge"] = recharge_data[value_col].shift(1) - recharge_data[value_col]
    if len(recharge_data) > 0:
        fig_r, ax_r = plt.subplots(figsize=(10, 4))
        ax_r.plot(
            recharge_data["Date"],
            recharge_data["Recharge"],
            marker="o",
            color="#2ca02c",
            label="Recharge (m)",
        )
        ax_r.axhline(0, color="#888888", linestyle="--", linewidth=1)
        ax_r.set_xlabel("Date")
        ax_r.set_ylabel("Recharge (m)")
        ax_r.legend()
        ax_r.grid(True, linestyle="--", alpha=0.6)
        plt.xticks(rotation=45)
        st.pyplot(fig_r)
        st.info(f"Average Recharge ({label}): {recharge_data['Recharge'].mean():.2f} m")
    else:
        st.warning(f"No recharge data available for {label}.")
