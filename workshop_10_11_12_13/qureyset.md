``` shell
>>> from core.models import Author, Post 
>>> Author.objects.all()
<QuerySet [<Author: Luka>, <Author: Giorgi>]>
>>> for author in Author.objects.all():
...     print(author.name)
... 
Luka
Giorgi
>>> Author.objects.first()
<Author: Luka>
>>> Author.objects.order_by("birthdate").first()
<Author: Luka>
>>> Author.objects.order_by("-birthdate").first()
<Author: Luka>
>>> Author.objects.order_by("-create_date").first()
<Author: Giorgi>
>>> Author.objects.order_by("create_date").first() 
<Author: Luka>
>>> Author.objects.order_by("create_date").last()     
<Author: Giorgi>
>>> Post.objects.filter(text="test")             
<QuerySet []>
>>> Post.objects.filter(text="Test")
<QuerySet [<Post: Test>, <Post: Test>]>
>>> Post.objects.filter(text="Test")
<QuerySet []>
>>> Post.objects.filter(text__contains="test")
<QuerySet [<Post: Test>, <Post: Test>]>
>>> Post.objects.create(author=Author.objects.last(), title="From terminal", text="This is created from terminal")
<Post: From terminal>
>>> Post.objects.last()
<Post: From terminal>
>>> last_post = Post.objects.last()
>>> last_post.author.name
'Giorgi'
>>> last_post.text
'This is created from terminal'
>>> last_post.title
'From terminal'
>>> last_post.text"
  File "<console>", line 1
    last_post.text"
                  ^
SyntaxError: unterminated string literal (detected at line 1)
>>> last_post.text += "(Updated)"
>>> last_post.text
'This is created from terminal(Updated)'
>>> last_post.text = "This is created from terminal (Updated)"
>>> last_post.text
'This is created from terminal (Updated)'
>>> last_post.text
'This is created from terminal (Updated)'
>>> last_post.save()
>>> Post.objects.get(pk=3)
<Post: Test>
>>> Post.objects.get(pk=3).title
'Test'
>>> Post.objects.get(pk=3).text   
'This is a big text (test)'
>>> Post.objects.get(id=3).text
'This is a big text (test)'
>>> Post.objects.filter(text__startswith="test")
<QuerySet []>
>>> Post.objects.count()                        
4
>>> Post.objects.filter(text__startswith="test").count() 
0
>>> post = Post.objects.get(pk=3)
>>> post
<Post: Test>
>>> post.title
'Test'
>>> post.pk
3
>>> post.id
3
>>> post.text
'This is a big text (test)'
>>> post.delete()
(1, {'core.Post': 1})
>>> author = Author.objects.get(pk=2)                        
>>> author.name
'Giorgi'
>>> Post.objects.create(author=author, title="Terminal 2"
... , text="Terminal text body") 
<Post: Terminal 2>
```