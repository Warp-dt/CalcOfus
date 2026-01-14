#!/bin/bash
xvfb-run -a streamlit run calcofus_web_app.py   --server.port=8501 \
                                                --server.address=0.0.0.0