import streamlit as st
import time
import random
import json
import google.generativeai as genai


# ==========================================
# 1. TRANSLATIONS & DATA (i18n)
# ==========================================

# 10 Daily Facts
FACTS = [
    {
        "EN": "**Shinkansen Delay**\nThe average delay of the Shinkansen is only about 18 seconds. If a train is delayed by more than 5 minutes, staff will bow to apologize and issue 'delay certificates' to passengers.",
        "JP": "**新幹線の遅延**\n新幹線の平均遅延時間はわずか18秒ほどです。5分以上遅れると、乗務員は謝罪し、乗客に「遅延証明書」を発行します。",
        "VI": "**Sự chậm trễ của Shinkansen**\nĐộ trễ trung bình của tàu cao tốc Shinkansen chỉ khoảng 18 giây. Nếu trễ quá 5 phút, nhân viên sẽ cúi đầu xin lỗi và phát 'giấy xác nhận trễ tàu' cho hành khách."
    },
    {
        "EN": "**More Pets Than Children**\nAccording to Japan Today, the number of pets (dogs and cats) in Japan is higher than the number of children under the age of 15.",
        "JP": "**子供より多いペット**\n『ジャパン・トゥデイ』によると、日本のペット（犬・猫）の数は、15歳未満の子供の数よりも多いそうです。",
        "VI": "**Thú cưng nhiều hơn trẻ em**\nTheo Japan Today, số lượng thú cưng (chó, mèo) tại Nhật Bản nhiều hơn so với số lượng trẻ em dưới 15 tuổi."
    },
    {
        "EN": "**Inemuri (居眠り)**\nInemuri is the culture of napping in public or at work; it is seen as a sign of dedication and exhaustion from hard work, rather than laziness.",
        "JP": "**居眠り**\n居眠りは公共の場や職場での仮眠の文化で、怠慢ではなく、仕事に尽くして疲れ果てた証拠と見なされます。",
        "VI": "**Inemuri (居眠り)**\nInemuri là văn hóa ngủ gật nơi công cộng hoặc công sở, được coi là dấu hiệu của sự tận tâm, làm việc kiệt sức chứ không phải lười biếng."
    },
    {
        "EN": "**Fastest Spoken Language**\nJapanese is considered one of the fastest-spoken languages in the world based on the number of syllables pronounced per second.",
        "JP": "**最も速く話される言語**\n日本語は、1秒あたりの音節数に基づくと、世界で最も話す速度が速い言語の一つとされています。",
        "VI": "**Ngôn ngữ nói nhanh nhất**\nTiếng Nhật được coi là một trong những ngôn ngữ có tốc độ phát âm nhanh nhất thế giới (tính theo số âm tiết mỗi giây)."
    },
    {
        "EN": "**20 Ways to Say Sorry**\nThere are at least 20 ways to say 'sorry' in Japanese, depending on the severity of the mistake and the person you are addressing.",
        "JP": "**20通りの謝罪**\n犯したミスの重さや相手との関係に応じて、日本語には少なくとも20通りの謝罪の仕方があります。",
        "VI": "**20 cách nói xin lỗi**\nCó ít nhất 20 cách để nói 'xin lỗi' trong tiếng Nhật, tùy thuộc vào mức độ lỗi lầm và đối tượng bạn đang nói chuyện."
    },
    {
        "EN": "**Geographical Surnames**\nMost Japanese surnames are related to geography, such as Tanaka (Inside the rice field) or Yamamoto (At the foot of the mountain).",
        "JP": "**地理的な苗字**\n日本人の苗字の多くは地理に関係しており、例えば「田中」（田んぼの中）や「山本」（山のふもと）などがあります。",
        "VI": "**Họ liên quan đến địa lý**\nHầu hết họ của người Nhật đều liên quan đến địa lý, ví dụ: Tanaka (Trong cánh đồng), Yamamoto (Dưới chân núi)."
    },
    {
        "EN": "**Wabi-sabi**\nWabi-sabi is the philosophy of finding beauty in imperfection and decay, such as a cracked ceramic bowl repaired with gold (Kintsugi), making it more precious and unique.",
        "JP": "**わびさび**\nわびさびは、欠けた陶器を金で修復する「金継ぎ」のように、不完全さや経年変化の中に美しさを見出す哲学であり、それによって物はより貴重で唯一無二のものになります。",
        "VI": "**Wabi-sabi**\nWabi-sabi là triết lý tìm thấy vẻ đẹp đỉnh cao trong sự không hoàn hảo và tàn phai theo thời gian, chẳng hạn như bát gốm nứt hàn lại bằng vàng."
    },
    {
        "EN": "**Safety**\nJapan is one of the safest countries in the world, to the extent that 6-year-old children can take the subway to school alone.",
        "JP": "**安全性**\n日本は世界で最も安全な国の一つであり、6歳の子供が一人で地下鉄に乗って通学できるほどです。",
        "VI": "**Sự an toàn**\nNhật Bản là một trong những nước an toàn nhất thế giới, đến mức trẻ em 6 tuổi có thể tự đi tàu điện ngầm một mình đến trường."
    },
    {
        "EN": "**Earthquake Alerts**\nEvery phone sold in Japan is required to have a rapid earthquake/tsunami alert system that sounds even if the phone is on silent mode.",
        "JP": "**緊急地震速報**\n日本で販売されるすべての携帯電話には、マナーモードでも鳴る緊急地震速報・津波警報システムの搭載が義務付けられています。",
        "VI": "**Cảnh báo động đất**\nMọi điện thoại bán ra tại Nhật đều bắt buộc có hệ thống cảnh báo động đất/sóng thần cực nhanh, phát âm thanh báo động kể cả khi để chế độ im lặng."
    },
    {
        "EN": "**Rice Paddy Art**\nIn Inakadate village, residents plant different colors of rice to create giant murals (like the Mona Lisa or Samurai) visible from above.",
        "JP": "**田んぼアート**\n田舎館村では、住民が色の異なる稲を植えて、上空から見える巨大な絵（モナリザや侍など）を描く「田んぼアート」を行っています。",
        "VI": "**Tranh trên ruộng lúa**\nTại làng Inakadate, người dân trồng các loại lúa có màu sắc khác nhau để tạo ra những bức tranh khổng lồ nhìn từ trên cao."
    }
]

# Learning Hub Topics
LEARNING_TOPICS = [
    {
        "title": {"EN": "Networking & Dining", "JP": "ネットワーキングと食事", "VI": "Bữa tiệc giao lưu / Đi ăn"},
        "img": "https://www.shutterstock.com/image-photo/diverse-group-social-event-people-600nw-2578529149.jpg",
        "desc": {"EN": "Goal: Ice-breaking and showing politeness.", "JP": "目的：アイスブレイクと礼儀正しさを示すこと。", "VI": "Mục tiêu là phá vỡ tảng băng (ice-breaking) và thể hiện sự lịch thiệp."},
        "phrases": [
            {"jp": "お疲れ様です。乾杯！", "romaji": "Otsukaresama desu. Kanpai!", "vi": "Chào mọi người và nâng ly.", "en": "Cheers / Good work today!"},
            {"jp": "これ、美味しいですね。おすすめは何ですか？", "romaji": "Kore, oishii desu ne. Osusume wa nan desu ka?", "vi": "Món này ngon nhỉ, bạn có gợi ý món nào khác không?", "en": "This is delicious. What do you recommend?"},
            {"jp": "お飲み物、何か頼みましょうか？", "romaji": "Onomimono, nanika tanomimashou ka?", "vi": "Bạn có muốn gọi thêm đồ uống gì không?", "en": "Shall we order some drinks?"},
            {"jp": "今日はごちそうさまでした / 楽しかったです。", "romaji": "Kyou wa gochisousama deshita / Tanoshikatta desu.", "vi": "Cảm ơn vì bữa ăn / Hôm nay rất vui.", "en": "Thank you for the meal / I had a great time."}
        ]
    },
    {
        "title": {"EN": "Meetings", "JP": "会議", "VI": "Cuộc họp"},
        "img": "https://cdn.prod.website-files.com/62196607bf1b46c300301846/6568ae33daf5cb0b75e26ee6_frsoeroe7prviafnog2q.webp",
        "desc": {"EN": "Goal: Express opinions and confirm info professionally.", "JP": "目的：意見を述べ、専門的に情報を確認すること。", "VI": "Mục tiêu là đưa ra ý kiến, đề xuất hoặc xác nhận thông tin chuyên nghiệp."},
        "phrases": [
            {"jp": "一つ伺ってもよろしいでしょうか？", "romaji": "Hitotsu ukagattemo yoroshii deshou ka?", "vi": "Tôi có thể hỏi một câu được không?", "en": "May I ask a question?"},
            {"jp": "その点については、賛成です。", "romaji": "Sono ten ni tsuite wa, sansei desu.", "vi": "Về điểm đó thì tôi đồng ý.", "en": "I agree on that point."},
            {"jp": "おっしゃることは分かりますが、こういう考え方はどうでしょうか？", "romaji": "Ossharu koto wa wakarimasu ga, kou iu kangaekata wa dou deshou ka?", "vi": "Tôi hiểu ý bạn, nhưng nếu suy nghĩ thế này thì sao?", "en": "I understand your point, but how about this perspective?"},
            {"jp": "念のため、もう一度確認させてください。", "romaji": "Nen no tame, mou ichido kakunin sasete kudasai.", "vi": "Để cho chắc chắn, xin cho phép tôi xác nhận lại một lần nữa.", "en": "Just to be sure, let me confirm once more."}
        ]
    },
    {
        "title": {"EN": "Small Talk", "JP": "雑談", "VI": "Giao tiếp hành lang (Small Talk)"},
        "img": "https://www.englishradar.com/wp-content/uploads/2017/10/Business-English-small-talk-FI.jpg",
        "desc": {"EN": "Goal: Building Rapport with colleagues.", "JP": "目的：同僚とのラポール（信頼関係）を築くこと。", "VI": "Dùng để xây dựng mối quan hệ (Building Rapport) với đồng nghiệp/cấp trên."},
        "phrases": [
            {"jp": "週末は何か予定ありますか？", "romaji": "Shuumatsu wa nanika yotei arimasu ka?", "vi": "Cuối tuần bạn có dự định gì không?", "en": "Do you have any plans for the weekend?"},
            {"jp": "最近、お忙しいですか？", "romaji": "Saikin, oisogashii desu ka?", "vi": "Dạo này bạn có bận lắm không?", "en": "Have you been busy lately?"},
            {"jp": "最近、〇〇にハマっているんです。", "romaji": "Saikin, 〇〇 ni hamatte iru n desu.", "vi": "Dạo này tôi đang khá là thích/mê 〇〇.", "en": "I've been really into 〇〇 lately."}
        ]
    },
    {
        "title": {"EN": "Visiting a House", "JP": "家を訪問する", "VI": "Thăm nhà người Nhật"},
        "img": "https://www.insidehook.com/wp-content/uploads/2022/12/House-Guests.jpg?fit=1200%2C800",
        "desc": {"EN": "Goal: Showing respect as a guest.", "JP": "目的：ゲストとして敬意を払うこと。", "VI": "Thể hiện sự tôn trọng khi làm khách."},
        "phrases": [
            {"jp": "お邪魔します。", "romaji": "Ojama shimasu.", "vi": "Xin lỗi vì đã làm phiền/ngắt quãng không gian của bạn.", "en": "Pardon my intrusion."},
            {"jp": "お招きいただき、ありがとうございます。", "romaji": "Omaneki itadaki, arigatou gozaimasu.", "vi": "Cảm ơn bạn rất nhiều vì đã mời tôi đến.", "en": "Thank you for inviting me."},
            {"jp": "素敵なお部屋ですね。", "romaji": "Suteki na oheya desu ne.", "vi": "Căn phòng/ngôi nhà đẹp quá nhỉ.", "en": "What a lovely room/house."},
            {"jp": "そろそろ失礼します。", "romaji": "Sorosoro shitsurei shimasu.", "vi": "Cũng đã đến lúc tôi xin phép phải về rồi.", "en": "I should be going soon."}
        ]
    },
    {
        "title": {"EN": "Omiyage (Gifting)", "JP": "お土産", "VI": "Văn hóa Omiyage (Quà tặng)"},
        "img": "https://media.npr.org/assets/img/2023/12/15/gettyimages-1339248145_custom-a26320d0a15c9bcbf59f7204df568c8e9c49f5dd.jpg",
        "desc": {"EN": "Goal: Giving gifts to colleagues or partners.", "JP": "目的：同僚やパートナーへの贈り物。", "VI": "Sử dụng khi bạn muốn tặng quà cho cá nhân, đối tác hoặc đồng nghiệp."},
        "phrases": [
            {"jp": "つまらないものですが...", "romaji": "Tsumaranai mono desu ga...", "vi": "Tuy là món đồ không có gì đặc biệt nhưng... (hạ thấp vật chất, đề cao tấm lòng).", "en": "It's nothing special, but..."},
            {"jp": "心ばかりの品ですが、お受け取りください。", "romaji": "Kokorobakari no shina desu ga, ouketori kudasai.", "vi": "Đây là chút tấm lòng của tôi, xin hãy nhận cho.", "en": "This is just a small token of my appreciation, please accept it."},
            {"jp": "お口に合うと嬉しいです。", "romaji": "Okuchi ni au to ureshii desu.", "vi": "Hy vọng món này hợp khẩu vị của bạn.", "en": "I hope it suits your taste."},
            {"jp": "皆様で召し上がってください。", "romaji": "Minasama de meshiagatte kudasai.", "vi": "Mời mọi người cùng thưởng thức ạ.", "en": "Please enjoy this with everyone."}
        ]
    },
    {
        "title": {"EN": "Directions & Moving", "JP": "道案内と移動", "VI": "Hỏi đường & Di chuyển"},
        "img": "https://ktvntd.edu.vn/wp-content/uploads/tmp/hoi-nguoi-qua-duong-trong-tieng-anh-du-lich.jpg",
        "desc": {"EN": "Goal: Navigating the city.", "JP": "目的：街をナビゲートすること。", "VI": "Sử dụng khi đi công tác, đi thực địa hoặc du lịch."},
        "phrases": [
            {"jp": "〇〇駅へはどう行けばいいですか？", "romaji": "〇〇 eki e wa dou ikeba ii desu ka?", "vi": "Làm sao để đi đến ga 〇〇 ạ?", "en": "How do I get to 〇〇 station?"},
            {"jp": "出口はどちらでしょうか？", "romaji": "Deguchi wa dochira deshou ka?", "vi": "Lối ra ở hướng nào thế nhỉ?", "en": "Which way is the exit?"},
            {"jp": "切符の買い方を教えていただけますか？", "romaji": "Kippu no kaikata o oshiete itadakemasu ka?", "vi": "Bạn chỉ giúp tôi cách mua vé được không?", "en": "Could you teach me how to buy a ticket?"},
            {"jp": "ここから歩いて行けますか？", "romaji": "Koko kara aruite ikemasu ka?", "vi": "Từ đây có thể đi bộ đến đó được không?", "en": "Can I walk there from here?"}
        ]
    },
    {
        "title": {"EN": "Interviews", "JP": "面接", "VI": "Phỏng vấn & Giới thiệu bản thân"},
        "img": "https://images.careerviet.vn/content/images/cac-loai-hinh-phong-van-careerbuilder.jpg",
        "desc": {"EN": "Goal: Show professionalism and readiness.", "JP": "目的：プロフェッショナリズムと準備を示すこと。", "VI": "Mục tiêu: Thể hiện thái độ chuyên nghiệp, cầu thị."},
        "phrases": [
            {"jp": "御社の理念に共感いたしました。", "romaji": "Onsha no rinen ni kyoukan itashimashita.", "vi": "Tôi rất đồng cảm/ấn tượng với triết lý của quý công ty.", "en": "I deeply resonate with your company's philosophy."},
            {"jp": "これまでの経験を活かしたいです。", "romaji": "Koremade no keiken o ikashitai desu.", "vi": "Tôi muốn phát huy những kinh nghiệm đã tích lũy.", "en": "I want to utilize my past experiences."},
            {"jp": "精一杯頑張ります。", "romaji": "Seiippai ganbarimasu.", "vi": "Tôi sẽ nỗ lực hết sức mình.", "en": "I will do my absolute best."},
            {"jp": "本日はお時間をいただき、ありがとうございました。", "romaji": "Honjitsu wa ojikan o itadaki, arigatou gozaimashita.", "vi": "Cảm ơn bạn đã dành thời gian cho tôi ngày hôm nay.", "en": "Thank you for taking the time today."}
        ]
    },
    {
        "title": {"EN": "Shopping & Services", "JP": "買い物とサービス", "VI": "Mua sắm & Dịch vụ"},
        "img": "https://www.tastingtable.com/img/gallery/the-clever-way-grocery-stores-stock-products/l-intro-1660768883.jpg",
        "desc": {"EN": "Goal: Purchasing and asking product info.", "JP": "目的：購入や製品情報を尋ねること。", "VI": "Mục tiêu: Giao dịch chính xác, hỏi thông tin sản phẩm."},
        "phrases": [
            {"jp": "〇〇を探しているんですが、ありますか？", "romaji": "〇〇 o sagashite iru n desu ga, arimasu ka?", "vi": "Tôi đang tìm 〇〇, cửa hàng có bán không ạ?", "en": "I'm looking for 〇〇, do you have it?"},
            {"jp": "試着してもいいですか？", "romaji": "Shichaku shitemo ii desu ka?", "vi": "Tôi có thể mặc thử món này được không?", "en": "May I try this on?"},
            {"jp": "プレゼント用にお願いします。", "romaji": "Purezento you ni onegai shimasu.", "vi": "Làm ơn gói giúp tôi theo dạng quà tặng.", "en": "Please wrap this as a gift."},
            {"jp": "カードで払えますか？", "romaji": "Kaado de haraemasu ka?", "vi": "Tôi có thể thanh toán bằng thẻ được không?", "en": "Can I pay by card?"}
        ]
    },
    {
        "title": {"EN": "Emergencies", "JP": "緊急事態", "VI": "Khẩn cấp (Emergencies)"},
        "img": "https://4850175.fs1.hubspotusercontent-na1.net/hubfs/4850175/04-Blog/Emergency-Signage.jpg",
        "desc": {"EN": "Goal: Seeking immediate help.", "JP": "目的：即座に助けを求めること。", "VI": "Mục tiêu: Phát tín hiệu cầu cứu rõ ràng để nhận trợ giúp."},
        "phrases": [
            {"jp": "助けてください！", "romaji": "Tasukete kudasai!", "vi": "Làm ơn hãy giúp tôi với!", "en": "Please help me!"},
            {"jp": "警察を呼んでください。", "romaji": "Keisatsu o yonde kudasai.", "vi": "Làm ơn hãy gọi cảnh sát giúp tôi.", "en": "Please call the police."},
            {"jp": "財布をなくしました。交番はどこですか？", "romaji": "Saifu o nakushimashita. Kouban wa doko desu ka?", "vi": "Tôi bị mất ví rồi. Đồn cảnh sát (Kouban) ở đâu ạ?", "en": "I lost my wallet. Where is the police box?"},
            {"jp": "救急車をお願いします！", "romaji": "Kyuukyuusha o onegai shimasu!", "vi": "Làm ơn gọi xe cấp cứu giúp tôi!", "en": "Please call an ambulance!"}
        ]
    },
    {
        "title": {"EN": "Praise & Feedback", "JP": "褒め言葉とフィードバック", "VI": "Phản hồi & Khen ngợi"},
        "img": "https://www.shutterstock.com/image-photo/compliment-praise-message-sign-business-600nw-2129756312.jpg",
        "desc": {"EN": "Goal: Encourage and build positive atmosphere.", "JP": "目的：励まし、肯定的な雰囲気を築くこと。", "VI": "Mục tiêu: Xây dựng bầu không khí tích cực và khích lệ."},
        "phrases": [
            {"jp": "すごいですね！", "romaji": "Sugoi desu ne!", "vi": "Giỏi quá nhỉ! / Tuyệt vời thật đấy!", "en": "That's amazing!"},
            {"jp": "さすがですね。", "romaji": "Sasuga desu ne.", "vi": "Quả nhiên là bạn! (Đúng như tôi mong đợi).", "en": "I'd expect nothing less from you."},
            {"jp": "勉強になります。", "romaji": "Benkyou ni narimasu.", "vi": "Tôi đã học hỏi được rất nhiều.", "en": "I've learned a lot from this."},
            {"jp": "いつも助かっています。", "romaji": "Itsumo tasukatte imasu.", "vi": "Lúc nào cũng nhờ có bạn giúp đỡ.", "en": "You're always a great help."}
        ]
    }
]

TRANSLATIONS = {
    "EN": {
        "culture_context": "Culture & Context", "culture_label": "Cultural Context", "culture_workplace": "Japanese Workplace", "culture_daily": "Daily Life", "culture_event": "Traditional Event",
        "relationship_label": "Relationship", "rel_boss": "Boss / Senior", "rel_colleague": "Colleague / Teammate", "rel_client": "Client / Business Partner", "rel_friend": "Friend",
        "purpose_title": "Purpose", "purpose_label": "What do you want to do?", "purp_convey": "Convey politely", "purp_opinion": "Give opinion / proposal", "purp_request": "Make a request", "purp_thanks": "Say thank you", "purp_apologize": "Apologize", "purp_decline": "Decline",
        "fact_title": "💡 1 Day 1 Fact",
        "msg_analysis": "Message Analysis", "input_label": "Enter your Japanese text here:", "input_placeholder": "Example: 明日時間ありますか？相談したいことあります。", "analyze_btn": "✨ Analyze", "error_empty": "Please enter some Japanese text to analyze.", "analyzing": "AI is analyzing the cultural nuance...", "analysis_complete": "Analysis Complete!",
        "formality": "Formality Level", "naturalness": "Naturalness", "relevance": "Context Relevance", "overall": "🎯 Overall Evaluation", "culture_exp": "⛩️ Culture Explanation", "rewrite_sugg": "✍️ Rewrite Suggestions", "related_expr": "📚 Related Expressions",
        "history_title": "🕒 Search History", "search_kw": "🔍 Search keywords...", "filter_context": "Filter by Context", "all_contexts": "All Contexts", "sort_date": "Sort by Date", "sort_new": "Newest First", "sort_old": "Oldest First", "view_detail": "View Detail", "delete": "Delete", "deleted": "Deleted!",
        "about_hero_title": "Master Japanese, Use JAPANI now", "about_hero_sub": "Our mission is to help you build true, natural communication through in-depth analysis of culture nuance", "our_solution": "Our Solution",
        "sol1_title": "Advanced Context Analysis", "sol1_desc": "AI analyzes relationships, environment, and emotional nuances. Not just translating, but understanding context.",
        "sol2_title": "Unspoken Cultural Rules", "sol2_desc": "Analyze implicit rules in Japanese communication including: Keigo, Tone, and Social protocols.",
        "sol3_title": "Smart Learning History", "sol3_desc": "Store and analyze interaction history. Provide personalized learning suggestions.",
        "ready": "Ready to master Japanese?", "get_started": "GET STARTED NOW",
        "nav_home": "🏠 Home", "nav_history": "🕒 History", "nav_learning": "📚 Learning Hub", "nav_generate": "✍️ AI Generate", "nav_settings": "⚙️ Settings", "nav_about": "ℹ️ About",
        "gen_title": "AI Generate Sentence", "gen_ctx": "Context", "gen_ctx_rest": "Restaurant", "gen_ctx_school": "School", "gen_ctx_office": "Office", "gen_ctx_interv": "Interview", "gen_ctx_cs": "Customer Service", "gen_ctx_date": "Dating", "gen_ctx_travel": "Travel", "gen_ctx_social": "Social Media", "gen_ctx_hospital": "Hospital", "gen_ctx_sales": "Sales",
        "gen_goal": "What do you want to say?", "gen_goal_ph": "Example: I want to cancel my reservation...", "gen_btn": "Generate Japanese Sentence",
        "set_title": "Settings", "set_theme": "Theme", "set_voice": "AI Voice", "set_length": "Response Length", "set_hist": "Save History", "set_auto": "Auto Suggestions", "set_sound": "Sound", "set_font": "Font Size", "set_logout": "Logout", "set_save": "Save Settings"
    },
    "JP": {
        "culture_context": "文化と背景", "culture_label": "文化的背景", "culture_workplace": "日本の職場", "culture_daily": "日常生活", "culture_event": "伝統行事",
        "relationship_label": "関係性", "rel_boss": "上司 / 先輩", "rel_colleague": "同僚 / チームメイト", "rel_client": "クライアント / 取引先", "rel_friend": "友人",
        "purpose_title": "目的", "purpose_label": "何を伝えたいですか？", "purp_convey": "丁寧に伝える", "purp_opinion": "意見・提案をする", "purp_request": "お願いをする", "purp_thanks": "感謝を伝える", "purp_apologize": "謝罪する", "purp_decline": "断る",
        "fact_title": "💡 1日1豆知識",
        "msg_analysis": "メッセージ分析", "input_label": "ここに日本語を入力してください:", "input_placeholder": "例: 明日時間ありますか？相談したいことあります。", "analyze_btn": "✨ 分析する", "error_empty": "分析する日本語を入力してください。", "analyzing": "AIが文化的ニュアンスを分析しています...", "analysis_complete": "分析完了！",
        "formality": "丁寧さ", "naturalness": "自然さ", "relevance": "文脈の適切さ", "overall": "🎯 総合評価", "culture_exp": "⛩️ 文化的な解説", "rewrite_sugg": "✍️ 書き換えの提案", "related_expr": "📚 関連表現",
        "history_title": "🕒 検索履歴", "search_kw": "🔍 キーワード検索...", "filter_context": "文脈で絞り込む", "all_contexts": "すべての文脈", "sort_date": "日付順", "sort_new": "新しい順", "sort_old": "古い順", "view_detail": "詳細を見る", "delete": "削除", "deleted": "削除しました！",
        "about_hero_title": "日本語をマスターしよう。今すぐJAPANIへ", "about_hero_sub": "私たちの使命は、文化のニュアンスを深く分析することで、真の自然なコミュニケーションを築く手助けをすることです", "our_solution": "私たちのソリューション",
        "sol1_title": "高度な文脈分析", "sol1_desc": "AIが関係性、環境、感情のニュアンスを分析します。単なる翻訳ではなく、文脈を理解します。",
        "sol2_title": "暗黙の文化ルール", "sol2_desc": "敬語、トーン、社会的プロトコルなど、日本のコミュニケーションにおける暗黙のルールを分析します。",
        "sol3_title": "スマートな学習履歴", "sol3_desc": "対話履歴を保存・分析し、パーソナライズされた学習の提案を行います。",
        "ready": "日本語をマスターする準備はできましたか？", "get_started": "今すぐ始める",
        "nav_home": "🏠 ホーム", "nav_history": "🕒 履歴", "nav_learning": "📚 学習ハブ", "nav_generate": "✍️ AI文章生成", "nav_settings": "⚙️ 設定", "nav_about": "ℹ️ 概要",
        "gen_title": "AI 文章生成", "gen_ctx": "文脈", "gen_ctx_rest": "レストラン", "gen_ctx_school": "学校", "gen_ctx_office": "オフィス", "gen_ctx_interv": "面接", "gen_ctx_cs": "カスタマーサービス", "gen_ctx_date": "デート", "gen_ctx_travel": "旅行", "gen_ctx_social": "SNS", "gen_ctx_hospital": "病院", "gen_ctx_sales": "営業",
        "gen_goal": "何を伝えたいですか？", "gen_goal_ph": "例：予約をキャンセルしたいのですが...", "gen_btn": "日本語の文章を生成",
        "set_title": "設定", "set_theme": "テーマ", "set_voice": "AI音声", "set_length": "応答の長さ", "set_hist": "履歴を保存", "set_auto": "自動提案", "set_sound": "サウンド", "set_font": "フォントサイズ", "set_logout": "ログアウト", "set_save": "設定を保存"
    },
    "VI": {
        "culture_context": "Văn hóa & Bối cảnh", "culture_label": "Bối cảnh văn hóa", "culture_workplace": "Nơi làm việc Nhật Bản", "culture_daily": "Đời sống hàng ngày", "culture_event": "Sự kiện truyền thống",
        "relationship_label": "Mối quan hệ", "rel_boss": "Sếp / Tiền bối", "rel_colleague": "Đồng nghiệp / Cùng nhóm", "rel_client": "Khách hàng / Đối tác", "rel_friend": "Bạn bè",
        "purpose_title": "Mục đích", "purpose_label": "Bạn muốn làm gì?", "purp_convey": "Truyền đạt lịch sự", "purp_opinion": "Đưa ý kiến / đề xuất", "purp_request": "Đưa ra yêu cầu", "purp_thanks": "Nói lời cảm ơn", "purp_apologize": "Xin lỗi", "purp_decline": "Từ chối",
        "fact_title": "💡 Mỗi ngày 1 kiến thức",
        "msg_analysis": "Phân tích tin nhắn", "input_label": "Nhập văn bản tiếng Nhật của bạn vào đây:", "input_placeholder": "Ví dụ: 明日時間ありますか？相談したいことあります。", "analyze_btn": "✨ Phân tích", "error_empty": "Vui lòng nhập văn bản tiếng Nhật để phân tích.", "analyzing": "AI đang phân tích sắc thái văn hóa...", "analysis_complete": "Hoàn tất phân tích!",
        "formality": "Mức độ trang trọng", "naturalness": "Mức độ tự nhiên", "relevance": "Độ phù hợp bối cảnh", "overall": "🎯 Đánh giá tổng thể", "culture_exp": "⛩️ Giải thích văn hóa", "rewrite_sugg": "✍️ Đề xuất viết lại", "related_expr": "📚 Các cách diễn đạt liên quan",
        "history_title": "🕒 Lịch sử tìm kiếm", "search_kw": "🔍 Tìm kiếm từ khóa...", "filter_context": "Lọc theo bối cảnh", "all_contexts": "Tất cả bối cảnh", "sort_date": "Sắp xếp theo ngày", "sort_new": "Mới nhất trước", "sort_old": "Cũ nhất trước", "view_detail": "Xem chi tiết", "delete": "Xóa", "deleted": "Đã xóa!",
        "about_hero_title": "Làm chủ tiếng Nhật, Dùng JAPANI ngay", "about_hero_sub": "Sứ mệnh của chúng tôi là giúp bạn xây dựng sự giao tiếp tự nhiên, chân thực thông qua phân tích chuyên sâu về sắc thái văn hóa", "our_solution": "Giải pháp của chúng tôi",
        "sol1_title": "Phân tích bối cảnh nâng cao", "sol1_desc": "AI phân tích quan hệ, môi trường và sắc thái cảm xúc. Không chỉ dịch, mà còn hiểu ngữ cảnh thực tế.",
        "sol2_title": "Quy tắc văn hóa ngầm", "sol2_desc": "Phân tích quy tắc ngầm trong giao tiếp Nhật Bản bao gồm: Keigo, Tone, và Social protocols.",
        "sol3_title": "Lịch sử học tập thông minh", "sol3_desc": "Lưu trữ và phân tích lịch sử tương tác. Đưa ra gợi ý học tập cá nhân hóa dành riêng cho bạn.",
        "ready": "Sẵn sàng làm chủ tiếng Nhật chưa?", "get_started": "BẮT ĐẦU NGAY",
        "nav_home": "🏠 Trang chủ", "nav_history": "🕒 Lịch sử", "nav_learning": "📚 Góc học tập", "nav_generate": "✍️ AI Viết câu", "nav_settings": "⚙️ Cài đặt", "nav_about": "ℹ️ Giới thiệu",
        "gen_title": "AI Đề xuất viết câu", "gen_ctx": "Bối cảnh", "gen_ctx_rest": "Nhà hàng", "gen_ctx_school": "Trường học", "gen_ctx_office": "Văn phòng công ty", "gen_ctx_interv": "Phỏng vấn xin việc", "gen_ctx_cs": "Chăm sóc khách hàng", "gen_ctx_date": "Hẹn hò / Tình cảm", "gen_ctx_travel": "Du lịch", "gen_ctx_social": "Mạng xã hội", "gen_ctx_hospital": "Bệnh viện / Phòng khám", "gen_ctx_sales": "Bán hàng / Tư vấn",
        "gen_goal": "Mục đích / Nội dung bạn muốn nói là gì?", "gen_goal_ph": "Ví dụ: Mình muốn xin nghỉ phép vào thứ 6 tuần sau vì có việc gia đình...", "gen_btn": "✨ Tạo câu Tiếng Nhật",
        "set_title": "Cài đặt Hệ thống", "set_theme": "Giao diện (Sáng/Tối)", "set_voice": "Giọng AI", "set_length": "Độ dài phản hồi", "set_hist": "Lưu lịch sử tìm kiếm", "set_auto": "Gợi ý tự động", "set_sound": "Âm thanh hệ thống", "set_font": "Cỡ chữ", "set_logout": "Đăng xuất", "set_save": "Lưu cài đặt"
    }
}

def t(key):
    lang = st.session_state.get("lang_switcher", "VI")
    return TRANSLATIONS.get(lang, TRANSLATIONS["EN"]).get(key, key)

# ==========================================
# 2. PAGE CONFIG & STYLES
# ==========================================
st.set_page_config(page_title="JAPANI - AI Japanese Assistant", page_icon="💬", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Noto+Sans+JP:wght@300;400;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', 'Noto Sans JP', sans-serif; }
[data-testid="stAppViewContainer"] { background-color: #F0F8FF; }
[data-testid="stHeader"] { background-color: transparent; }
[data-testid="stVerticalBlockBorderWrapper"] { 
    background-color: #FFFFFF; 
    border-radius: 12px; 
    border: none; 
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); 
}
h1, h2, h3, h4, h5, h6 { color: #0a192f; font-weight: 600; }

.stButton > button {
    background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%); color: #FFFFFF;
    border-radius: 12px; border: none; padding: 0.6rem 1.5rem;
    font-weight: bold; transition: all 0.3s ease; width: 100%;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2);
}
.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4); color: white; }

.glass-card {
    background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px);
    border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); padding: 1.5rem;
    transition: transform 0.3s ease; margin-bottom: 1rem;
}
.glass-card:hover { transform: translateY(-3px); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08); }

.gradient-text {
    background: linear-gradient(90deg, #1E3A8A, #3B82F6);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

[data-testid="stSidebar"] { background-color: #FFFFFF; border-right: 1px solid #E5E7EB; }
.stTextArea textarea { border-radius: 8px; border: 1px solid #E5E7EB; padding: 1rem; }
.stProgress > div > div > div > div { background-color: #1E3A8A; }
.suggestion-box {
    background-color: #E0F2FE; border: 1px solid #BAE6FD;
    border-radius: 8px; padding: 1rem; margin-bottom: 0.5rem; color: #0a192f;
}
.topic-img { width: 100%; height: 160px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. REAL AI FUNCTIONS (Gemini API)
# ==========================================
def get_gemini_api_key():
    if "GEMINI_API_KEY" in st.secrets:
        return st.secrets["GEMINI_API_KEY"]
    return None

def init_genai():
    api_key = get_gemini_api_key()
    if api_key:
        genai.configure(api_key=api_key)
        return True
    return False

def analyze_japanese_text(text, culture, relationship, purpose, lang="EN"):
    if not init_genai():
        st.error("API Key is missing. Please configure GEMINI_API_KEY in Streamlit Secrets.")
        st.stop()
    
    prompt = f"""
    You are an expert Japanese linguist and cultural consultant.
    Analyze the following Japanese text: "{text}"
    Context: {culture}
    Relationship: {relationship}
    Purpose: {purpose}
    Target Explanation Language: {lang} (EN/JP/VI)
    
    Provide your analysis strictly in the following JSON format without any markdown wrappers or extra text:
    {{
        "formality": <int between 0-100>,
        "naturalness": <int between 0-100>,
        "relevance": "<High/Medium/Low>",
        "overall": "<Short overall evaluation in {lang}>",
        "culture_explanation": "<Cultural explanation in {lang}>",
        "rewrite_suggestions": ["<Japanese rewrite 1>", "<Japanese rewrite 2>"],
        "related_expressions": ["<Related Japanese phrase 1>", "<Related Japanese phrase 2>"]
    }}
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        st.error(f"AI API Error: {str(e)}")
        st.stop()

def generate_japanese_sentence(context, goal, lang="EN"):
    if not init_genai():
        st.error("API Key is missing. Please configure GEMINI_API_KEY in Streamlit Secrets.")
        st.stop()
        
    prompt = f"""
    You are a native Japanese speaker.
    Generate a natural and culturally appropriate Japanese sentence for the following situation:
    Context: {context}
    Goal: {goal}
    Target Explanation Language: {lang} (EN/JP/VI)
    
    Provide the result strictly in the following JSON format without any markdown wrappers:
    {{
        "res": "<The generated Japanese sentence>",
        "exp": "<Explanation of why this sentence is natural and appropriate, written in {lang}>"
    }}
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        st.error(f"AI API Error: {str(e)}")
        st.stop()

# ==========================================
# 4. LAYOUT & NAVIGATION
# ==========================================
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown("<h2 class='gradient-text' style='margin: 0; padding: 0; font-size: 2.2rem;'>💬 JAPANI</h2>", unsafe_allow_html=True)
with col3:
    st.radio("Language", ["EN", "JP", "VI"], index=2, horizontal=True, label_visibility="collapsed", key="lang_switcher")
st.markdown("<hr style='margin-top: 0.5rem; margin-bottom: 2rem;'/>", unsafe_allow_html=True)

# Generate Random Fact for today
if 'daily_fact_index' not in st.session_state:
    st.session_state.daily_fact_index = random.randint(0, len(FACTS)-1)

st.sidebar.markdown("### Navigation")
page = st.sidebar.radio("Go to", [t("nav_home"), t("nav_history"), t("nav_learning"), t("nav_generate"), t("nav_settings"), t("nav_about")], label_visibility="collapsed")
st.sidebar.divider()

current_lang = st.session_state.get("lang_switcher", "VI")

# ==========================================
# 5. PAGE LOGIC
# ==========================================
if page == t("nav_home"):
    with st.sidebar:
        st.markdown(f"### {t('culture_context')}")
        culture = st.selectbox(t("culture_label"), [t("culture_workplace"), t("culture_daily"), t("culture_event")])
        relationship = st.selectbox(t("relationship_label"), [t("rel_boss"), t("rel_colleague"), t("rel_client"), t("rel_friend")])
        st.markdown(f"### {t('purpose_title')}")
        purpose = st.radio(t("purpose_label"), [t("purp_convey"), t("purp_opinion"), t("purp_request"), t("purp_thanks"), t("purp_apologize"), t("purp_decline")])

    st.markdown(f"### {t('msg_analysis')}")
    col_input, col_result = st.columns([3, 2])

    with col_input:
        with st.container(border=True):
            input_text = st.text_area(t("input_label"), height=200, placeholder=t("input_placeholder"), max_chars=1000)
            analyze_clicked = st.button(t("analyze_btn"), type="primary")

        if analyze_clicked:
            if not input_text:
                st.error(t("error_empty"))
            else:
                with st.spinner(t("analyzing")):
                    st.session_state.analysis_results = analyze_japanese_text(input_text, culture, relationship, purpose, current_lang)
        
        if 'analysis_results' in st.session_state:
            res = st.session_state.analysis_results
            with st.container(border=True):
                st.markdown(f"<h4 style='color: #1E3A8A; margin-bottom: 1rem;'>📊 AI Analysis</h4>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns(3)
                with c1: st.metric(t("formality"), f"{res['formality']}%"); st.progress(res['formality']/100)
                with c2: st.metric(t("naturalness"), f"{res['naturalness']}%"); st.progress(res['naturalness']/100)
                with c3: st.metric(t("relevance"), res['relevance']); st.progress(0.8)
                st.markdown("---")
                st.markdown(f"#### {t('overall')}")
                st.write(res['overall'])

    with col_result:
        if 'analysis_results' in st.session_state:
            res = st.session_state.analysis_results
            with st.container(border=True):
                st.markdown(f"#### {t('culture_exp')}")
                st.info(res['culture_explanation'])
            with st.container(border=True):
                st.markdown(f"#### {t('rewrite_sugg')}")
                for s in res['rewrite_suggestions']: st.markdown(f'<div class="suggestion-box">{s}</div>', unsafe_allow_html=True)
            with st.container(border=True):
                st.markdown(f"#### {t('related_expr')}")
                for e in res['related_expressions']: st.markdown(f"- {e}")

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown(f"### {t('fact_title')}")
    st.info(FACTS[st.session_state.daily_fact_index][current_lang])

elif page == t("nav_history"):
    st.markdown(f"## {t('history_title')}")
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1: st.text_input(t('search_kw'), max_chars=100)
    with c2: st.selectbox(t('filter_context'), [t('all_contexts'), t('rel_boss'), t('rel_colleague')])
    with c3: st.selectbox(t('sort_date'), [t('sort_new'), t('sort_old')])
    st.markdown("---")
    
    for _ in range(2):
        st.markdown(f"""
        <div class="glass-card">
            <span style="color: #6B7280; font-size: 0.875rem;">2024-05-15 10:30</span>
            <h4 style="margin-top: 0.5rem; color: #0a192f;">明日時間ありますか？相談したいことあります。</h4>
            <span style="background: #E0F2FE; color: #1E3A8A; padding: 0.25rem 0.75rem; border-radius: 999px;">{t("rel_boss")}</span>
        </div>
        """, unsafe_allow_html=True)
        a1, a2, _ = st.columns([1, 1, 8])
        with a1: st.button(t('view_detail'), key=f"v_{_}", use_container_width=True)
        with a2: st.button(t('delete'), key=f"d_{_}", use_container_width=True)

elif page == t("nav_learning"):
    st.markdown(f"## {t('nav_learning')}")
    st.write("Chọn một chủ đề để khám phá các mẫu câu phổ biến:" if current_lang == "VI" else ("トピックを選んでください：" if current_lang == "JP" else "Select a topic to explore common phrases:"))
    
    # Grid of topics
    cols = st.columns(2)
    for i, topic in enumerate(LEARNING_TOPICS):
        col = cols[i % 2]
        with col:
            with st.expander(topic['title'][current_lang]):
                if topic['img']:
                    st.markdown(f"<img src='{topic['img']}' class='topic-img'>", unsafe_allow_html=True)
                st.info(topic['desc'][current_lang])
                for phrase in topic['phrases']:
                    st.markdown(f"""
                    <div class="suggestion-box">
                        <strong style="color:#1E3A8A; font-size:1.1rem;">{phrase['jp']}</strong><br>
                        <span style="color:#6B7280; font-size:0.9rem;">{phrase['romaji']}</span><br>
                        <span style="color:#4B5563;">{phrase[current_lang.lower()]}</span>
                    </div>
                    """, unsafe_allow_html=True)

elif page == t("nav_generate"):
    st.markdown(f"## {t('gen_title')}")
    ctxs = [t("gen_ctx_rest"), t("gen_ctx_school"), t("gen_ctx_office"), t("gen_ctx_interv"), t("gen_ctx_cs"), t("gen_ctx_date"), t("gen_ctx_travel"), t("gen_ctx_social"), t("gen_ctx_hospital"), t("gen_ctx_sales")]
    selected_ctx = st.selectbox(t("gen_ctx"), ctxs)
    goal = st.text_area(t("gen_goal"), height=100, placeholder=t("gen_goal_ph"))
    
    if st.button(t("gen_btn"), type="primary"):
        if goal:
            with st.spinner("Generating..."):
                res = generate_japanese_sentence(selected_ctx, goal, current_lang)
                st.success("Success!")
                st.markdown(f"""
                <div class="glass-card" style="border-left: 4px solid #3B82F6;">
                    <h3 style="color:#1E3A8A; margin-bottom: 0.5rem;">{res['res']}</h3>
                    <p style="color:#4B5563; margin:0;">{res['exp']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Please enter your goal.")

elif page == t("nav_settings"):
    st.markdown(f"## {t('set_title')}")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.selectbox(t("set_theme"), ["Light", "Dark", "System Default"])
        st.selectbox(t("set_voice"), ["Male", "Female", "Young", "Elderly"])
        st.slider(t("set_length"), 1, 10, 5)
        st.slider(t("set_font"), 12, 24, 16)
    with c2:
        st.toggle(t("set_hist"), value=True)
        st.toggle(t("set_auto"), value=True)
        st.toggle(t("set_sound"), value=False)
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.button(t("set_save"), type="primary")
        st.button(t("set_logout"))
    st.markdown("</div>", unsafe_allow_html=True)

elif page == t("nav_about"):
    st.markdown(f"""
    <div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, #1E3A8A 0%, #0a192f 100%); border-radius: 16px; color: white; margin-bottom: 3rem;">
        <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem;">{t('about_hero_title')}</h1>
        <p style="font-size: 1.25rem; opacity: 0.9;">{t('about_hero_sub')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h2 style='text-align: center; margin-bottom: 2rem;'>{t('our_solution')}</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    def sol_card(icon, title, desc):
        return f'<div class="glass-card" style="text-align: center; height: 100%;"><div style="font-size: 3rem; margin-bottom: 1rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));">{icon}</div><h3 class="gradient-text">{title}</h3><p style="color: #4B5563; text-align: left; line-height: 1.6;">{desc}</p></div>'
    
    with c1: st.markdown(sol_card("🧠", t('sol1_title'), t('sol1_desc')), unsafe_allow_html=True)
    with c2: st.markdown(sol_card("⛩️", t('sol2_title'), t('sol2_desc')), unsafe_allow_html=True)
    with c3: st.markdown(sol_card("📈", t('sol3_title'), t('sol3_desc')), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align: center; padding: 3rem; background-color: #E0F2FE; border-radius: 16px;">
        <h2 style="color: #0a192f; margin-bottom: 1.5rem;">{t('ready')}</h2>
    </div>
    """, unsafe_allow_html=True)
    _, col_center, _ = st.columns([1, 1, 1])
    with col_center:
        st.button(t('get_started'), type="primary", use_container_width=True)
