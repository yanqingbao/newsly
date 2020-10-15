# base-image
FROM python:3.8



# Set working directory
WORKDIR .

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .


# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'



# expose streamlit port
EXPOSE 8501

# run streamlit
CMD ["streamlit", "run", "main.py"]