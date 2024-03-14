import os
import streamlit as st

# Function to search for gitignore files in the resource folder and subfolder contents of it 


# def search_gitignore_files(resource_folder,appendName=''):
#     gitignore_files = []
#     for filename in os.listdir(resource_folder):
#         if filename.endswith(".gitignore"):
#             gitignore_files.append(appendName,filename)
#     return gitignore_files

def search_gitignore_files(root_folder):
    gitignore_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".gitignore"):
                root = root.replace(root_folder,"")
                gitignore_files.append(root+"\\"+ file)
    return gitignore_files




# Function to read the content of a gitignore file
def read_gitignore_file(filename):
    with open(os.path.join(filename), "r") as file:
        content = file.read()
    return content

# Main function to run the Streamlit app
def main():

    st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 500px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

    st.sidebar.title("Gitignore File Generator")

     # Information about the source of gitignore files
    st.sidebar.write("Gitignore files sourced from: [github/gitignore](https://github.com/github/gitignore)")

     # Information about the source of gitignore files
    st.sidebar.write("Feel free to contribute to this project!:  [Gitignore-File-Generator](https://github.com/AdarshBP/Gitignore-File-Generator)")
    
    # Information about gitignore files
    st.sidebar.markdown("""
    1. The root folder contains templates for commonly used programming languages and technologies. These provide a meaningful set of rules to help you get started and ensure that unimportant files are not committed into your repository.
    2. Global templates include rules for various editors, tools, and operating systems that can be used in different situations. It's recommended to either add these to your global template or merge them into your project-specific templates if you intend to use them permanently.
    3. Community templates consist of specialized rules for other popular languages, tools, and projects that may not belong in mainstream templates. These should be added to your project-specific templates when you decide to adopt the framework or tool.
    """)

    # Main content area for output
    st.title("Gitignore File Content")
    
    gitignore_files :list= []
    # Search for gitignore files
    resource_folder = "resource"
    gitignore_files.extend(search_gitignore_files(resource_folder))
    
    # Display search results
    if not gitignore_files:
        st.write("No gitignore files found in the resource folder.")
    else:
        selected_file = st.selectbox("Select a gitignore file:", gitignore_files)
        st.write(f"Selected gitignore file: {selected_file}")
        
        # Display gitignore data
        gitignore_content = read_gitignore_file(resource_folder+"//"+selected_file)
        st.code(gitignore_content, language="plaintext")

if __name__ == "__main__":
    main()
