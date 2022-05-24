mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"thiago.blima@hotmail.com\"\n\
"> ~/.streamlit/config.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

