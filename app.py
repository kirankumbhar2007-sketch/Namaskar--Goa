from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')

# HERITAGE PAGE
@app.route('/heritage')
def heritage():
    return render_template('heritage.html')

# SAKHI AI PAGE
@app.route('/sakhi')
def sakhi():
    return render_template('sakhi.html')

# CULTURAL PASSPORT PAGE
@app.route('/passport')
def passport():
    return render_template('passport.html')

# COMMUNITY IMPACT PAGE
@app.route('/impact')
def impact():
    return render_template('impact.html')

# SAKHI AI CHAT RESPONSE ROUTE
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').lower()

    # ===== SAKHI RESPONSES =====

    if 'fort' in user_message or 'aguada' in user_message:
        response = "🏰 Aguada Fort was built in 1612 by the Portuguese! Did you know it once held 2.4 million litres of fresh water to supply ships? Our AI avatar — a Portuguese soldier from that era — can narrate its full story. I can also connect you with local guide Raju who knows every hidden corner. Want me to book a heritage walk? ₹500 goes 100% directly to Raju's family! 🌟"

    elif 'basilica' in user_message or 'bom jesus' in user_message or 'church' in user_message:
        response = "⛪ The Basilica of Bom Jesus is a UNESCO World Heritage Site! It holds the remains of St. Francis Xavier, preserved for over 400 years. Our AI-reconstructed priest avatar narrates 500 years of miracles and mystery. Entry is free but donations go directly to the local restoration community. Want me to arrange a guided heritage tour? 🙏"

    elif 'food' in user_message or 'eat' in user_message or 'restaurant' in user_message or 'xacuti' in user_message:
        response = "🍛 You MUST try authentic Goan food! I recommend Aunty Maria's home kitchen in Fontainhas — she still cooks Sorpotel and Bebinca using her great-grandmother's 200-year-old recipe. Booking through Namaskar Goa means 100% of your ₹800 meal cost goes directly to her. No middlemen, no tour operators taking cuts. Shall I check her availability today? 🌶️"

    elif 'craft' in user_message or 'pottery' in user_message or 'kumbar' in user_message:
        response = "🏺 Amazing choice! The Kumbar pottery community has been crafting clay pots for 600 years. Master potter Ramesh offers 2-hour live workshops for ₹600. Only 8 active potters remain in Ponda village. Every rupee goes directly to Ramesh — our blockchain smart contract guarantees it. Want me to book a workshop slot for you? 🎨"

    elif 'kunbi' in user_message or 'weaving' in user_message or 'weave' in user_message:
        response = "🧵 The Kunbi weaving tradition is 800 years old and only 12 master weavers remain. Savitri Naik from Sattari is one of them. She offers 3-hour weaving workshops for ₹750 — and teaches you to create your own piece to take home! We've also digitally preserved her techniques in our AI Heritage Vault so this craft lives forever. Shall I book you in? 🌿"

    elif 'dance' in user_message or 'dekhnni' in user_message or 'music' in user_message or 'culture' in user_message:
        response = "🎭 Goa's classical Dekhnni dance blends Hindu and Portuguese traditions — and only 8 performers still know the authentic choreography! Nalini from Panaji offers intimate evening performances plus a 1-hour workshop for ₹1,200. Your booking goes 100% to Nalini's dance school. Want me to check tonight's availability? 💃"

    elif 'budget' in user_message or 'cheap' in user_message or 'cost' in user_message or 'price' in user_message or 'money' in user_message:
        response = "💰 Great question! Here's the Namaskar Goa experience range:\n\n🟢 ₹200–500 — Local village walk, street food tour\n🟡 ₹500–1,500 — Craft workshop, heritage guided tour\n🔵 ₹1,500–3,000 — Cooking class with local family, classical dance show\n🟣 ₹3,000–5,000 — Full-day cultural immersion package\n\nALL payments go 100% to locals. What's your daily budget? I'll build your perfect Cultural Journey Map! 🗺️"

    elif 'help' in user_message or 'emergency' in user_message or 'sos' in user_message or 'lost' in user_message or 'danger' in user_message:
        response = "🆘 EMERGENCY CULTURAL SOS ACTIVATED!\n\nI'm immediately connecting you to the nearest verified Local Guardian in your area. Please stay calm and stay where you are.\n\n📍 Nearest Guardian: Suresh Naik — 0.8km away — calling now\n🚨 Local authorities notified\n📞 Emergency: 112\n\nYou are NOT alone. Namaskar Goa has your back 24/7. Can you tell me your current location? 🙏"

    elif 'coin' in user_message or 'culture coin' in user_message or 'reward' in user_message or 'badge' in user_message:
        response = "🌟 Culture Coins are your Namaskar Goa reward currency! Every experience you book earns you coins:\n\n🏺 Craft Workshop = 150 coins\n🍛 Local Meal = 80 coins\n🏰 Heritage Tour = 120 coins\n🎭 Cultural Show = 200 coins\n\nCoins level you up: Wanderer → Traveler → Cultural Ambassador → Heritage Guardian → Living Legend 👑\n\nTop Cultural Ambassadors get SPONSORED by tourism boards! How many coins do you have so far? 🎮"

    elif 'blockchain' in user_message or 'payment' in user_message or 'middlemen' in user_message or 'direct' in user_message:
        response = "🔗 Our blockchain payment system is revolutionary! Here's how it works:\n\n1️⃣ You book an experience through Namaskar Goa\n2️⃣ A smart contract is created instantly\n3️⃣ Payment goes DIRECTLY to the local artisan/guide\n4️⃣ You see a real-time receipt showing exactly where every rupee went\n\nExample: Your ₹2,000 = ₹1,200 to Ramesh's homestay + ₹500 to pottery workshop + ₹300 to local restaurant.\n\nTransparent. Trustworthy. Revolutionary. 💎"

    elif 'ar' in user_message or 'augmented' in user_message or 'virtual' in user_message or 'ai avatar' in user_message:
        response = "🤖 Our AR + AI Story Narrator is the future of heritage tourism! Here's what happens:\n\n🏛️ Stand in front of Aguada Fort\n📱 Open Namaskar Goa AR mode\n👤 A hyper-realistic AI avatar of a 1612 Portuguese soldier appears\n🗣️ He narrates the fort's story IN THAT ERA — battles, secrets, hidden rooms\n🌐 Available in Hindi and English\n\nWe've trained AI on 500 years of historical records, oral traditions, and archived colonial documents. Want to experience it? Visit the Heritage page! ✨"

    elif 'local' in user_message or 'guide' in user_message or 'meet' in user_message or 'people' in user_message:
        response = "🙏 Meeting real locals is what Namaskar Goa is ALL about! Our verified local network includes:\n\n👨‍🏺 Ramesh Kumbar — Master Potter (⭐ 4.9 rating)\n👩‍🍳 Maria D'Souza — Heritage Cook (⭐ 5.0 rating)\n🧵 Savitri Naik — Kunbi Weaver (⭐ 4.8 rating)\n🎭 Nalini Raut — Classical Dancer (⭐ 4.9 rating)\n🏰 Raju Fernandes — Fort Historian (⭐ 4.7 rating)\n\nAll verified, rated, and paid directly. Who would you like to meet? 🌴"

    elif 'goa' in user_message or 'visit' in user_message or 'travel' in user_message or 'trip' in user_message:
        response = "🌴 Welcome to the REAL Goa that no guidebook shows you! Beyond the beaches and nightlife lies:\n\n🏛️ 500-year-old forts with untold stories\n🍛 200-year-old recipes in family kitchens\n🧵 800-year-old crafts nearly extinct\n🎭 Classical dances with only 8 performers left\n🏘️ Villages unchanged for centuries\n\nTell me what excites you most — History, Food, Crafts, Adventure, or Spiritual experiences? I'll build your perfect Cultural Journey Map! 🗺️"

    elif 'itinerary' in user_message or 'plan' in user_message or 'schedule' in user_message or 'journey map' in user_message:
        response = "🗺️ Let me build your Cultural Journey Map! Answer these quickly:\n\n1️⃣ How many days in Goa?\n2️⃣ Interests: History / Food / Crafts / Adventure / Spiritual?\n3️⃣ Budget per day: Under ₹500 / ₹500–2000 / ₹2000+?\n4️⃣ Physical ability: Easy walks / Moderate / Active explorer?\n\nOnce you answer, I'll give you an hour-by-hour immersive itinerary with hidden local spots NO guidebook mentions! 🌟"

    elif 'hello' in user_message or 'hi' in user_message or 'namaste' in user_message or 'hey' in user_message or 'start' in user_message:
        response = "🙏 Namaskaram! I'm SAKHI — your Superintelligent AI for Cultural Heritage & Immersive travel in Goa!\n\nI know every hidden story, every endangered craft, every amazing local you MUST meet — and I make sure 100% of your money goes directly to the community.\n\nWhat brings you to Goa? Tell me your interests:\n🏛️ Ancient History\n🍛 Authentic Cuisine\n🎨 Traditional Crafts\n🌅 Hidden Experiences\n🕌 Spiritual Journeys\n\nOr just ask me anything! 🌴"

    elif 'thank' in user_message or 'thanks' in user_message or 'great' in user_message or 'awesome' in user_message:
        response = "🌴 You're so welcome! That's what I'm here for — to make your Goa experience genuinely transformative, not just touristic.\n\nRemember: every booking you make through Namaskar Goa directly empowers a local family. You're not just traveling — you're preserving 500 years of heritage. 🙏\n\nAnything else I can help you discover? The hidden Goa is waiting for you! ✨"

    elif 'passport' in user_message or 'level' in user_message or 'explorer' in user_message or 'wanderer' in user_message:
        response = "🎮 Your Cultural Passport is your badge of honour as a responsible traveler!\n\n🌱 Wanderer — Just starting out\n🌿 Traveler — 5+ local experiences\n🦋 Cultural Ambassador — 15+ experiences + community contribution\n🛡️ Heritage Guardian — Funded preservation of a dying art\n👑 Living Legend — Top 100 globally\n\nEach level unlocks exclusive experiences, sponsorships from tourism boards, and the ability to be featured on our Global Leaderboard! Check your passport at the Passport page 🏅"

    elif 'workshop' in user_message or 'learn' in user_message or 'class' in user_message or 'teach' in user_message:
        response = "🎨 Namaskar Goa offers incredible hands-on workshops directly with masters:\n\n🏺 Pottery with Ramesh — ₹600 (2 hours)\n🧵 Kunbi Weaving with Savitri — ₹750 (3 hours)\n🍛 Goan Cooking with Maria — ₹950 (2.5 hours)\n🎭 Dekhnni Dance with Nalini — ₹1,200 (2 hours + show)\n🎨 Azulejo Tile Painting — ₹500 (1.5 hours)\n\nAll workshops go directly to the master artisan. You also earn Culture Coins and a badge for each! Which one calls to you? 🌟"

    else:
        response = "🌴 Fascinating! I'm SAKHI and I know every secret Goa holds.\n\nHere's what I can help you with:\n🏛️ Heritage sites with AR narrators\n🍛 Authentic local food experiences\n🎨 Traditional craft workshops\n👥 Meet verified local artisans\n💰 Budget planning (zero middlemen)\n🗺️ Personalized Cultural Journey Maps\n🆘 Emergency SOS support\n🎮 Cultural Passport & badges\n\nWhat would you like to explore? The real Goa is waiting! 🙏"

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)