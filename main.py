from textblob import TextBlob

t1="bu bir deneme cümlesidir."
b1=TextBlob(t1)
e1=b1.translate(from_lang='tr', to='en')
print("Orijinal Metin:", b1)
print("İngilizce metin:", e1)
print(e1.sentiment)
if e1.sentiment.polarity>0:
      print('Bu cümle olumlu bir görüş içermektedir.')
elif e1.sentiment.polarity<0:
      print('Bu cümle olumsuz bir görüş içermektedir.')
else:
      print('Bu cümle bir duygu içermemektedir.Bu cümle bir bilgilendirme cümlesidir')
