
import webbrowser
def gs(stxt):
    txt='+'.join(stxt.split())
    url=f"https://www.google.com/search?q={txt}&btnK=Google+Search & sca_esv = 584340551 & sxsrf = AM9HkKn5DKm4gJ9l1ljkOoR2s3zlgmY3Bw % 3A1700588748625 & source = hp & ei = zOxcZf69I4f_ptQPsJ6h2Aw & iflsig = AO6bgOgAAAAAZVz63I84HNY - j7T7bGOddo - Mkh2IHr5m"
    ''.join(url)
    webbrowser.open(url)
    return "search result has been displayed"
gs('how to cook mohanthaal')