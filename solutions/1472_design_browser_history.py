class Page:

    def __init__(self, val:str = '', next=None, prev=None):
        self.val:str = val
        self.next:Page = next
        self.prev:Page = prev


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.currentPage = Page(homepage)
        
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        newPage = Page(url, prev=self.currentPage)
        self.currentPage.next = newPage
        self.currentPage = newPage
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        
        while self.currentPage.prev and steps > 0:
            self.currentPage = self.currentPage.prev
            steps -= 1
        return self.currentPage.val


        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.currentPage.next and steps > 0:
            self.currentPage = self.currentPage.next
            steps -= 1
        return self.currentPage.val
        


# Your BrowserHistory object will be instantiated and called as such:
browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       #// You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     #// You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      #// You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   #// You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   #// You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                #// You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     #// You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                #// You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   #// You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   #// You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"