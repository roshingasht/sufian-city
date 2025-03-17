from flask import Flask, request
import requests

app = Flask(__name__)

def get_client_ip(request):
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  
    else:
        ip = request.remote_addr  
    return ip

def is_iranian_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json?token=1fa07b3902021a")
        data = response.json()
        
        print(f"Response from ipinfo.io: {data}")
        
        country = data.get("country", "")
        
        if country == "IR":
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/')
def home():
    ip = get_client_ip(request)
    
    if is_iranian_ip(ip):
        return f"آی‌پی شما ثبت شد: {ip}"
    else:
        return "لطفاً فیلترشکن خود را خاموش کنید و دوباره امتحان کنید."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)