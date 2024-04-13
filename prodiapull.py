from prodiapy import Prodia
import os

prodia = Prodia(
    api_key = os.getenv('PRODIA_API_KEY')

)

job = prodia.sd.generate(prompt="a cat with a big sombrero and smoking a cigar")
result = prodia.wait(job)


print(result.image_url)