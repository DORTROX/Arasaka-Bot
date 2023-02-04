import requests
r = requests.post(
    "https://api.deepai.org/api/cyberpunk-generator",
    data={
        'text': 'YOUR_TEXT_URL',
    },
    headers={'api-key': '228cc8e1-88f5-4c8b-94d0-eada85d1b442'}
)
print(r.json())

{"status":"success","jobs":[{"id":"CeRPN9csET9TerKhnyYp","path":"/jobs/CeRPN9csET9TerKhnyYp","created":1675450571613,"user":"zktrMEQqyucEJUB1VqGs64R2P1k1","userInfo":{"id":"zktrMEQqyucEJUB1VqGs64R2P1k1","displayName":"Akshat Rana"},"status":"queued","progress":0,"modStatus":"unmoderated","title":"Immortals fighting","archived":false,"isPublic":false,"dateMeta":{"isWithinYear":true,"isWithinMonth":true,"isWithinWeek":true,"isWithinDay":true,"isWithinHour":true},"collectionsMeta":{"isCollectedByCreator":false,"numCollections":0},"jobType":"text","algorithm":"diffusion2","preset":"NightCafe","prompts":["Immortals fighting","detailed matte painting, deep color, fantastical, intricate detail, splash screen, complementary colors, fantasy concept art, 8k resolution trending on Artstation Unreal Engine 5"],"promptWeights":[1,0.9],"sdEngine":"stable-diffusion-v1-5","sampler":"k_lms","promptWeight":0.5,"runtime":"short","resolution":"thumb","seed":3413035698,"aspectRatio":"1:1","initWeight":0,"numImages":4,"paymentStatus":"paid"}]}