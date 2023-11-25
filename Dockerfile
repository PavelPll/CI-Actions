FROM cdrx/pyinstaller-linux
#ENV PATH="/root/miniconda3/bin:${PATH}"
#ENV DEBIAN_FRONTEND=noninteractive

RUN pip install numpy tqdm
