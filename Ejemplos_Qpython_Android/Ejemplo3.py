import json
import androidhelper
droid=androidhelper.Android()

ret=droid.scanBarcode().result
print('\n',ret)

res=json.dumps(ret, ensure_ascii=False)
y=json.loads(res)
numero=y['extras']['SCAN_RESULT']

print('El numero es: ', numero)
result=droid.ttsSpeak(numero)

for i in y['extras']['SCAN_RESULT']:
    print('-', i)
    result=droid.ttsSpeak(i)
