from pywebio import start_server
from app import main  # استيراد الدالة الرئيسية من ملف التطبيق

if __name__ == "__main__":
    start_server(main, port=8080)  # تشغيل التطبيق على المنفذ 8080
