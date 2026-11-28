import os
import random
import logging
from html import escape
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(PROJECT_DIR, "en")
EN_GUIDES_DIR = os.path.join(EN_DIR, "guides")

EN_GUIDES_META = {
    "binance-reg.html": ("How to Register on Binance and Complete Verification in 2026", "binance-reg.png", "Crypto Basics"),
    "ai-crypto-trading.html": ("Using AI for Cryptocurrency Market Analysis", "ai-crypto-trading.png", "AI & Trading"),
    "crypto-wallet-safety.html": ("Crypto Wallet Security: How to Protect Your Digital Assets", "crypto-wallet-safety.png", "Security"),
    "p2p-trading-guide.html": ("P2P Trading Guide: How to Safely Buy and Sell Crypto", "p2p-trading-guide.png", "P2P Trading"),
    "binance-grid-bot.html": ("Setting Up a Spot Grid Bot on Binance: Automated Trading for Beginners", "binance-grid-bot.png", "Trading Bots"),
    "binance-earn-guide.html": ("How to Earn Passive Income with Binance Earn: Complete Staking Guide", "binance-earn-guide.png", "Passive Income"),
    "crypto-futures-trading.html": ("Introduction to Crypto Futures: How to Minimize Risk and Avoid Liquidation", "crypto-futures-trading.png", "Futures"),
    "crypto-technical-analysis.html": ("Technical Analysis Basics: How to Read Crypto Charts and Find Entry Points", "crypto-technical-analysis.png", "Analytics"),
    "altcoin-fundamental-analysis.html": ("How to Research Altcoins Before Buying: Fundamental Analysis Guide", "altcoin-fundamental-analysis.png", "Investing"),
    "binance-square-guide.html": ("How to Use Binance Square to Spot Strong Crypto Trends and Insights", "binance-square-guide.png", "Traffic & Blogs"),
    "crypto-risk-management.html": ("Advanced Risk Management: How Not to Lose Your Deposit on Binance in 2026", "crypto-risk-management.png", "Pro Trading"),
    "ai-memecoin-analysis.html": ("Local AI vs. Memecoins: How to Spot Gem Tokens in 2026", "ai-memecoin-thumb.png", "AI & Memecoins"),
    "crypto-trading-psychology.html": ("Crypto Trading Psychology & AI: How to Beat Emotional Trading with Algorithms", "crypto-trading-psychology.png", "Psychology & AI"),
    "ai-phishing-protection.html": ("Protection Against AI Phishing and Deepfakes in Web3 in 2026", "ai-phishing-protection.png", "Web3 Security"),
    "ai-dca-strategy.html": ("DCA Strategy & Local AI: How to Safely Buy Crypto Dips in 2026", "ai-dca-strategy.png", "Strategies & AI"),
    "ai-crypto-agents-guide.html": ("AI Agents in Crypto: How to Build an Autonomous Market Analysis Assistant in 2026", "ai-crypto-agents-guide.png", "AI Agents")
}

EN_FOOTER_HTML = """
    <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <p>&copy; 2026 Crypto AI Hub. All rights reserved.</p>
        <p class="footer-note">Content is for informational purposes only and does not constitute financial advice.</p>
        <p style="margin: 8px 0 14px 0; font-size: 0.9rem;">
            <a href="/en/about.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">About Us</a> |
            <a href="/en/privacy.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">Privacy Policy</a> |
            <a href="/en/disclaimer.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">Disclaimer</a>
        </p>
        <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
            Join our Telegram Channel
        </a>
    </div>
"""


def build_related_en(current_file):
    others = [f for f in EN_GUIDES_META.keys() if f != current_file]
    selected = random.sample(others, min(3, len(others)))
    cards = ""
    for f_name in selected:
        title, img, badge = EN_GUIDES_META[f_name]
        cards += f"""
        <a href="{f_name}" class="related-card" style="text-decoration: none; background: #1e2026; border: 1px solid #2b3139; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column;">
            <img src="../../guides/{escape(img, quote=True)}" alt="{escape(title, quote=True)}" style="width: 100%; height: 130px; object-fit: cover;">
            <div style="padding: 15px;">
                <span style="color: #f3ba2f; font-size: 0.75rem; font-weight: bold; text-transform: uppercase;">{escape(badge)}</span>
                <h4 style="color: #fff; margin: 8px 0 0 0; font-size: 0.95rem; line-height: 1.4;">{escape(title)}</h4>
            </div>
        </a>
        """
    return f"""
    <section class="related-guides" style="margin-top: 40px; padding-top: 30px; border-top: 1px solid #2b3139;">
        <h3 style="color: #fff; margin: 0 0 20px 0; font-size: 1.4rem; border-left: 4px solid #f3ba2f; padding-left: 12px;">Related Guides</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px;">
            {cards}
        </div>
    </section>
    """


def patch_file(filepath, add_related=False):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # 1. Синхронизируем подвал
    footer = soup.find("footer")
    if footer:
        footer["class"] = "footer"
        footer.clear()
        footer.append(BeautifulSoup(EN_FOOTER_HTML, "html.parser"))

    # 2. Добавляем Related Guides в английские статьи
    if add_related and not soup.find("section", class_="related-guides"):
        promo_footer = soup.find("div", class_="promo-banner-footer")
        if promo_footer:
            rel_soup = BeautifulSoup(build_related_en(os.path.basename(filepath)), "html.parser")
            promo_footer.insert_after(rel_soup)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    logging.info(f"✅ Обновлено: {os.path.relpath(filepath, PROJECT_DIR)}")


def main():
    en_root = ["index.html", "wotd.html", "prompts.html", "calculator.html", "news.html", "partners.html", "about.html", "privacy.html", "disclaimer.html"]
    for p in en_root:
        patch_file(os.path.join(EN_DIR, p), add_related=False)

    if os.path.exists(EN_GUIDES_DIR):
        for fname in sorted(os.listdir(EN_GUIDES_DIR)):
            if fname.endswith(".html"):
                patch_file(os.path.join(EN_GUIDES_DIR, fname), add_related=True)


if __name__ == "__main__":
    main()
