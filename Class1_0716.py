
# coding: utf-8

# # 數值運算

# In[1]:


3+2*8


# In[2]:


a=3


# In[3]:


b=2


# In[4]:


a


# In[5]:


b


# In[6]:


a/b


# In[7]:


c=2.5
d=1.5


# In[8]:


type{c}


# In[9]:


type(c)


# In[10]:


c/d


# In[11]:


a='Hello world'


# In[12]:


type(a)


# In[13]:


int(a)


# In[14]:


a='2'


# In[15]:


a="2"


# In[16]:


type(a)


# In[17]:


int(a)


# In[18]:


float(a)


# In[19]:


a=5


# In[20]:


a+a


# In[21]:


a=10


# In[22]:


a+a


# # 範例 bookprice

# In[23]:


exchange_rate=32.33


# In[24]:


type(exchange_rate)


# In[25]:


price=25.6


# In[26]:


ntd_price=price * exchange_rate


# In[27]:


ntd_price


# In[30]:


round(ntd_price,2)


# # 字串

# In[31]:


get_ipython().run_line_magic('pinfo', 'round')


# In[32]:


a='hello world'


# In[33]:


a="hello world"


# In[34]:


"寶寶心理苦"


# In[35]:


a


# In[36]:


a
b


# In[37]:


print(a,b)


# In[39]:


print('use \n to')
# pirnt('\n')換行


# In[48]:


a='''1 2 3
100 200 300'''
print(a)


# In[49]:


a='''1\t2\t3
100\t200\t300'''
print(a)
# \t排版整齊


# In[50]:


a='hi this is a 1ong text'
print(a)
# \ 告知程式是同一行


# In[51]:


s='hello'


# In[52]:


s[0]
#數字從0開始


# In[53]:


s[1]


# In[54]:


len(s)


# In[55]:


s[len(s)-1]


# In[56]:


s[-1]
# 取最後一個字 倒數回來用負號


# In[57]:


#for(i=1; i<len(s);i++)
s[1:]


# In[58]:


#for(i=1; i<3;i++) 到3以前就停止
s[1:3]


# In[59]:


s='[請益] 面試與受訓時間衝突'


# In[60]:


s[1:]


# In[62]:


#for(i=0; i<len(s);i++)
s[::1]


# In[64]:


#for(i=0; i<len(s);i+2)
s[::2]


# In[65]:


s[5::2]


# In[66]:


# 正反倒裝
s[::-1]


# In[67]:


s='上海自來水來自海上'
s== s[::-1]


# In[69]:


s = 'hello'
s = s+'world'
s


# In[71]:


letter = '我要加薪!'
letter * 10


# In[73]:


dir(letter)
get_ipython().run_line_magic('pinfo', 'letter.capitalize')


# In[75]:


s='hello'
s.upper()


# In[76]:


s.lower()


# In[79]:


s='[請益] 面 試 與 受 訓 時 間 衝 突'
s.split()


# In[82]:


article='本季戰績不佳的紅雀在昨日宣布解雇總教練馬西尼（Mike Matheny），且在還沒確定接任的總教練以前，由板凳教練希爾（Mike Shildt）代理總教練一職。而根據《聖路易斯郵報》（St. Louis Post-Dispatch）的報導指出紅雀球團目前正苦於尋找新的教練來接替空缺的教頭位置，因此再三考量之下預計聘請前紐約洋基總教練Joe Girardi（吉拉迪）來遞補這個位置。'


# In[84]:


article.count('教練')


# In[86]:


article.replace('教練','Coach')

