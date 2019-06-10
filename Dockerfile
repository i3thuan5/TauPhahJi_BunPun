FROM i3thuan5/taigi_bunpun

RUN python manage.py startapp app
RUN mkdir -p app/management/commands/
RUN touch app/management/commands/__init__.py
RUN echo 'INSTALLED_APPS+=("app",)' >> hok8_bu7/settings.py

RUN pip install kau3-tian2-iong7-ji7

COPY 產生語句.py app/management/commands/
RUN python manage.py 產生語句
COPY 產生語言模型.py app/management/commands/
RUN python manage.py 產生語言模型
COPY 產生辭典.py ./
RUN python 產生辭典.py < ku.txt > su.txt
