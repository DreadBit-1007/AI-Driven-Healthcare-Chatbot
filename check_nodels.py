import google.generativeai as genai

genai.configure(api_key="AIzaSyClinWtFcuvOGz2lL1AhPJfWKoLg3n2dO0")

for model in genai.list_models():
    print(model.name, model.supported_generation_methods)
