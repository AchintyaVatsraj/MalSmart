import time

from pandas import read_csv
from selenium import webdriver

class ML_model:
    def web_url(self,url):
        sample_url = [url]
        data = read_csv('/home/kali/PycharmProjects/antimalware/urldata.csv')
        data.label.replace("good", 0, inplace=True)
        data.label.replace("bad", 1, inplace=True)
        detect = data['url']
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer()
        x = cv.fit_transform(detect)
        from sklearn.model_selection import train_test_split
        y = data.label
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        from sklearn.naive_bayes import MultinomialNB
        clf = MultinomialNB()
        clf.fit(X_train, y_train)
        clf.score(X_test, y_test)
        print("Accuracy of Model", clf.score(X_test, y_test) * 100, "%")
        vect = cv.transform(sample_url).toarray()
        output = clf.predict(vect)
        if output == 0:
            # print("not malicious")
            return 0
        else:
            # print("malicious")
            return 1






def webButtonOnClick():
    driver = webdriver.Chrome("/home/kali/PycharmProjects/antimalware/chromedriver")
    url = "https://google.com/"
    driver.get(url)
    ml = ML_model()
    while True:
        url_visited = driver.current_url
        url_visited = url_visited.replace("https://www.", "")
        url_visited = url_visited.replace("https://", "")
        url_visited = url_visited.replace("http://", "")
        print(url_visited)
        time.sleep(2)
        if ml.web_url(url_visited) == 0:
            print(url_visited, "not malicious")
        else:
            driver.get("http://malsmart.com")
            print(url_visited, "malicious")

webButtonOnClick()