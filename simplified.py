import streamlit as st
import pandas as pd
# =======================
# Example schedule data
# =======================
# schedule = [{'Course': 'PROG1', 'Session': 1, 'Instructor': 'Talal', 'Day': 'Sun', 'Time': 'T2'}, {'Course': 'PROG1', 'Session': 2, 'Instructor': 'Talal', 'Day': 'Sun', 'Time': 'T1'}, {'Course': 'PROG2', 'Session': 1, 'Instructor': 'Talal', 'Day': 'Sun', 'Time': 'T3'}, {'Course': 'PROG2', 'Session': 2, 'Instructor': 'Talal', 'Day': 'Sun', 'Time': 'T4'}, {'Course': 'MATH', 'Session': 1, 'Instructor': 'Giath', 'Day': 'Sun', 'Time': 'T1'}, {'Course': 'MATH', 'Session': 2, 'Instructor': 'Giath', 'Day': 'Mon', 'Time': 'T2'}, {'Course': 'ALGO', 'Session': 1, 'Instructor': 'Obai', 'Day': 'Wed', 'Time': 'T2'}, {'Course': 'ALGO', 'Session': 2, 'Instructor': 'Obai', 'Day': 'Wed', 'Time': 'T3'}]
schedule = [{'Course': 'PROG_1', 'Session': 1, 'Instructor': 'Talal', 'Day': 'Thu', 'Time': 'T2'}, {'Course': 'PROG_1', 'Session': 2, 'Instructor': 'Talal', 'Day': 'Thu', 'Time': 'T1'}, {'Course': 'PROG_2', 'Session': 1, 'Instructor': 'Talal', 'Day': 'Mon', 'Time': 'T3'}, {'Course': 'PROG_2', 'Session': 2, 'Instructor': 'Talal', 'Day': 'Mon', 'Time': 'T1'}, {'Course': 'PROG_lab_1', 'Session': 1, 'Instructor': 'Ola', 'Day': 'Sun', 'Time': 'T1'}, {'Course': 'PROG_lab_2', 'Session': 1, 'Instructor': 'Shaza', 'Day': 'Mon', 'Time': 'T2'}, {'Course': 'PROG_lab_3', 'Session': 1, 'Instructor': 'Ola', 'Day': 'Sun', 'Time': 'T3'}, {'Course': 'PROG_lab_4', 'Session': 1, 'Instructor': 'Shaza', 'Day': 'Sun', 'Time': 'T2'}, {'Course': 'MATH_1', 'Session': 1, 'Instructor': 'Giath', 'Day': 'Sun', 'Time': 'T3'}, {'Course': 'MATH_1', 'Session': 2, 'Instructor': 'Giath', 'Day': 'Sun', 'Time': 'T2'}, {'Course': 'ALGO_1', 'Session': 1, 'Instructor': 'Obai', 'Day': 'Wed', 'Time': 'T1'}, {'Course': 'ALGO_1', 'Session': 2, 'Instructor': 'Obai', 'Day': 'Mon', 'Time': 'T3'}, {'Course': 'ALGO_2', 'Session': 1, 'Instructor': 'Obai', 'Day': 'Mon', 'Time': 'T2'}, {'Course': 'ALGO_2', 'Session': 2, 'Instructor': 'Obai', 'Day': 'Mon', 'Time': 'T1'}, {'Course': 'ALGO_lab_1', 'Session': 1, 'Instructor': 'Said', 'Day': 'Thu', 'Time': 'T2'}, {'Course': 'ALGO_lab_2', 'Session': 1, 'Instructor': 'Said', 'Day': 'Thu', 'Time': 'T1'}, {'Course': 'PHY_1', 'Session': 1, 'Instructor': 'Giath', 'Day': 'Sun', 'Time': 'T1'}, {'Course': 'PHY_1', 'Session': 2, 'Instructor': 'Giath', 'Day': 'Mon', 'Time': 'T3'}]

df = pd.DataFrame(schedule)

# =======================
# Prepare display
# =======================
df["Display"] = df.apply(lambda r: f"{r['Course']}/D.{r['Instructor']}\n", axis=1)


# Pivot table: Day × Time, join multiple sessions per slot
timetable = df.pivot_table(
    index="Day",
    columns="Time",
    values="Display",
    aggfunc=lambda x: "\n---\n".join(x),
    fill_value="-"
)



day_order = ["Sun", "Mon", "Tue", "Wed", "Thu"]
time_order = ["T1", "T2","T3","T4"]


timetable = timetable.reindex(index=day_order, columns=time_order, fill_value="-")

# =======================
# Streamlit UI
# =======================

st.set_page_config(layout="wide")
st.title("📅 University Course Timetable")

# st.write("### Timetable View")
# st.dataframe(timetable, use_container_width=True)


# Optional: Styled HTML table
def render_html_table(df):
    html = '<table style="border-collapse: collapse; width: 100%;">'
    html += '<tr style="background-color:#4CAF50; color:white;"><th>Day / Time</th>'
    for t in df.columns:
        html += f"<th>{t}</th>"
    html += "</tr>"

    for idx, row in df.iterrows():
        html += f"<tr><td style='border:1px solid #333; padding:8px'>{idx}</td>"
        for val in row:
            html += f"<td style='border:1px solid #333; padding:8px; white-space:pre-line'>{val}</td>"
        html += "</tr>"
    html += "</table>"
    return html


st.markdown("### Timetable (Styled HTML)", unsafe_allow_html=True)
st.markdown(render_html_table(timetable), unsafe_allow_html=True)
