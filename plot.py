import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

attendance_data = pd.read_csv("attendance.csv")
status_data = pd.read_csv("student_status_history.csv")
status_data_semester_3 = status_data[status_data['Semester'] == 3]

merged_attendance_status = pd.merge(attendance_data, status_data_semester_3,
                                    left_on='User_Code', right_on='Student_Code')
merged_attendance_status["Status_Group"] = merged_attendance_status["Status"].apply(
    lambda x: 'THO' if x == 'THO' else 'Others'
)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Status_Group', y='Percentage', data=merged_attendance_status)
plt.title('Boxplot of Attendance Percentages: THO vs Others')
plt.xlabel('Status Group')
plt.ylabel('Attendance Percentage')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=merged_attendance_status, x='Percentage', hue='Status_Group', kde=True)
plt.title('Histogram of Attendance Percentages: THO vs Others')
plt.xlabel('Attendance Percentage')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total_Activity', y='Percentage', hue='Status_Group', data=merged_attendance_status)
plt.title('Scatter Plot of Total Activity vs Attendance Percentage')
plt.xlabel('Total Activity')
plt.ylabel('Attendance Percentage')
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(data=merged_attendance_status, x='Percentage', hue='Status_Group', fill=True)
plt.title('Density Plot of Attendance Percentages: THO vs Others')
plt.xlabel('Attendance Percentage')
plt.show()

plt.figure(figsize=(10, 6))
sns.ecdfplot(data=merged_attendance_status, x='Percentage', hue='Status_Group')
plt.title('Cumulative Distribution Plot of Attendance Percentages: THO vs Others')
plt.xlabel('Attendance Percentages')
plt.ylabel('Cumulative Probability')
plt.show()

avg_grade_data = pd.read_csv("avg_grade.csv")

merged_avg_status = pd.merge(avg_grade_data, status_data_semester_3,
                                    left_on='User_Code', right_on='Student_Code')
merged_avg_status["Status_Group"] = merged_avg_status["Status"].apply(
    lambda x: 'THO' if x == 'THO' else 'Others'
)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Status_Group', y='Average_Grade', data=merged_avg_status)
plt.title('Boxplot of Average Grades: THO vs Others')
plt.xlabel('Status Group')
plt.ylabel('Average Grades')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=merged_avg_status, x='Average_Grade', hue='Status_Group', kde=True)
plt.title('Histogram of Average Grades: THO vs Others')
plt.xlabel('Average Grades')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(data=merged_avg_status, x='Average_Grade', hue='Status_Group', fill=True)
plt.title('Density Plot of Average Grades: THO vs Others')
plt.xlabel('Average Grades')
plt.show()

plt.figure(figsize=(10, 6))
sns.ecdfplot(data=merged_avg_status, x='Average_Grade', hue='Status_Group')
plt.title('Cumulative Distribution Plot of Average Grades: THO vs Others')
plt.xlabel('Average Grades')
plt.ylabel('Cumulative Probability')
plt.show()

combined_data = pd.merge(merged_attendance_status[['User_Code', 'Percentage', 'Status_Group']], 
                         merged_avg_status[['User_Code', 'Average_Grade', 'Status_Group']], 
                         on='User_Code')

combined_data = combined_data[combined_data['Status_Group_x'] == combined_data['Status_Group_y']]
combined_data.drop(columns=['Status_Group_y'], inplace=True)
combined_data.rename(columns={'Status_Group_x': 'Status_Group'}, inplace=True)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Percentage', y='Average_Grade', hue='Status_Group', data=combined_data)
plt.title('Scatter Plot of Attendance Percentage vs Average Grade by Status Group')
plt.xlabel('Attendance Percentage')
plt.ylabel('Average Grade')
plt.show()

avg_grade_prefix_data = pd.read_csv("avg_grade_by_prefix.csv")

merged_grade_prefix_status_data = pd.merge(avg_grade_prefix_data, status_data_semester_3, left_on='User_Code', right_on='Student_Code')

merged_grade_prefix_status_data['Status_Group'] = merged_grade_prefix_status_data['Status_x'].apply(lambda x: 'THO' if x == 'THO' else 'Others')

merged_grade_prefix_status_data.drop(columns=['User_Login', 'Status_y', 'Semester_y', 'Term_ID_y', 'Major_ID_y', 'Campus_Code', 'Student_Code'], inplace=True)
merged_grade_prefix_status_data.rename(columns={'Semester_x': 'Semester', 'Term_ID_x': 'Term_ID', 'Major_ID_x': 'Major_ID', 'Campus': 'Campus_Code'}, inplace=True)

plt.figure(figsize=(14, 6))
sns.boxplot(x='Prefix_Subject', y='Average_Grade', hue='Status_Group', data=merged_grade_prefix_status_data)
plt.title('Boxplot of Average Grades by Subject Prefix and Status Group')
plt.xlabel('Subject Prefix')
plt.ylabel('Average Grade')
plt.xticks(rotation=45)
plt.legend(title='Status Group')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=merged_grade_prefix_status_data, x='Average_Grade', hue='Status_Group', kde=True)
plt.title('Histogram of Average Grades by Status Group')
plt.xlabel('Average Grade')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Semester', y='Average_Grade', hue='Status_Group', data=merged_grade_prefix_status_data)
plt.title('Scatter Plot of Semester vs Average Grade by Status Group')
plt.xlabel('Semester')
plt.ylabel('Average Grade')
plt.show()

# df1 = df1[["User_Login", "Percentage"]]

# df2 = pd.read_csv("avg_grade_ut2.csv")
# df2 = df2[["User_Login", "Average_Grade", "Fail_Count"]]

# df3 = pd.read_csv("avg_grade_onlyIT.csv")
# df3 = df3[["User_Login", "Avg_COM", "Fail_COM", "Avg_MOB", "Fail_MOB", "Avg_PRO", "Fail_PRO", "Avg_WEB", "Fail_WEB"]]



# merge_df = pd.merge(df1, df, on="User_Login")
# plt.figure(figsize=(10,6))
# sns.histplot(data=merge_df, x="Percentage", hue="Status", multiple="stack", bins=20)
# plt.title('Attendance - Dropout')
# plt.xlabel("Attendance rate")
# plt.ylabel("Number of dropout")
# plt.show()

# merge_df = pd.merge(df1, df, on="User_Login", how="inner")
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=merge_df, x="Semester", y="Percentage", hue="Status")
# plt.title("Attendance - Dropout")
# plt.xlabel("Semester")
# plt.ylabel("Attendance")
# plt.legend(title="Status")
# plt.show()

# merge_df = pd.merge(df2, df, on="User_Login", how="inner")
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=merge_df, x="Semester", y="Average_Grade", hue="Status")
# plt.title("Average_grade - Dropout")
# plt.xlabel("Semester")
# plt.ylabel("Average_grade")
# plt.legend(title="Status")
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.boxplot(data=merge_df, x="Semester", y="Fail_Count", hue="Status")
# plt.title("Fail_count - Dropout")
# plt.xlabel("Semester")
# plt.ylabel("Fail_count")
# plt.legend(title="Status")
# plt.show()

# merge_df = pd.merge(df2, df, on="User_Login", how='inner')
# merged_df = merge_df[merge_df['Semester'] <= 3]
# sns.pairplot(merged_df, hue='Status', diag_kind='kde', markers=["o", "s"])

# merge_df = pd.merge(df3, df, on="User_Login", how='inner')
# merged_df = merge_df[merge_df['Semester'] <= 3]
# sns.pairplot(merged_df, hue='Status', diag_kind='kde', markers=["o", "s"])

# status_mapping = {status: idx for idx, status in enumerate(df['Status'].unique())}
# df['Status_Code'] = df['Status'].map(status_mapping)

# subject_related_columns = [col for col in df3.columns if 'Fail_' in col or 'Avg_' in col]

# correlation_df = pd.merge(df3, df[['User_Login', 'Status_Code']], on="User_Login")
# correlation_df = correlation_df.drop('User_Login', axis=1)

# correlation_matrix = correlation_df.corr()

# plt.figure(figsize=(15, 10))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap between Subject Performance and Test Status')
# plt.show()

# df4 = pd.read_csv('avg_grade_by_subject.csv')
# df5 = pd.read_csv('subject_list.csv')

# dfm = df4.merge(df5, on='Subject_Code')[["Member_Login", "User_Code", "Value", "Subject_Code", "Skill_Code_x", "Semester","Number_Of_Credit_x", "Average_Grade", "Number_Of_Attempt"]]
# dfm.to_csv('merge.csv', sep=',', encoding='utf-8')