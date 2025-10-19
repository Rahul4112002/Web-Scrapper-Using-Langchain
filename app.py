# LangChain Web Scraper App (Streamlit)

# ========== Step 1: Import Dependencies ==========
# Ye sabhi libraries ko import karo jo project me use hongi
import streamlit as st
import chromedriver_autoinstaller # Selenium ke liye Chrome driver auto install karta hai
from langchain_community.document_loaders import (
    UnstructuredURLLoader, SeleniumURLLoader, WebBaseLoader
)

# Agar Selenium loader use karna hai toh Chrome driver ki jarurat hogi
chromedriver_autoinstaller.install() # Automatically download & install correct version

# Page ka title set karo aur layout wide rakho
st.set_page_config(page_title='LangChain Scraper', layout='wide')
st.title('LangChain Web Scraper')

# Sidebar pe dropdown se loader type select karwao
loader_choice = st.sidebar.selectbox(
    'Choose Scraper Loader',     # Hindi: Scraper loader choose karein
    ('Unstructured', 'Selenium', 'WebBase')
)

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...',
    'Mozilla/5.0 (X11; Linux x86_64)...',
    # Aur bhi agents add kar sakte ho
]
user_agent = st.sidebar.selectbox(
    'Choose User-Agent',
    user_agents
)

st.header('Enter Website Details') # Main section ka title
url = st.text_input('Enter Website URL', '')   # User se URL lo

if st.button('Scrape Content'):
    # Step 6.1: URL dala hai ya nahi check karo
    if not url:
        st.error('Please provide a website URL.')
    else:
        try:
            docs = []  # Documents in which scraped content ayega

            # Step 6.2: Loader selection logic
            if loader_choice == 'Unstructured':
                # Unstructured Loader se scraping
                loader = UnstructuredURLLoader(
                    urls=[url],
                    headers={'User-Agent': user_agent}
                )
                docs = loader.load()
            elif loader_choice == 'Selenium':
                # Selenium Loader se scraping
                loader = SeleniumURLLoader(
                    urls=[url],
                    headless=True,
                    browser='chrome'
                )
                docs = loader.load()
            elif loader_choice == 'WebBase':
                # WebBase Loader se scraping
                loader = WebBaseLoader(
                    url,
                    header_template={'User-Agent': user_agent}
                )
                docs = loader.load()

            # Step 6.3: Agar documents mile toh content extract karo
            if docs:
                content = '\n\n'.join(doc.page_content for doc in docs)
                # Sirf pehle 1000 characters preview me dikhao
                st.subheader('Extracted Content (First 1000 chars)')
                st.write(content[:1000])

                # Full content expander me dikhao + download ka option
                with st.expander('View Full Content'):
                    st.write(content)
                    st.download_button(label="Download Text",
                        data=content,
                        file_name="scraped_content.txt"
                    )
            else:
                st.warning('No content could be extracted.') # Hindi: Koi content nahi mila
        except Exception as e:
            st.error(f'Error: {e}') 