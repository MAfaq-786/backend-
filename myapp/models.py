from django.db import models

# Create your models here.

class Dashboard(models.Model):
    PAGE_CHOICES = [
        ("home", "Home / ہوم"),
        ("about", "About / بارے میں"),
        ("contact", "Contact / رابطہ کریں"),
        ("services", "Services / خدمات"),
        ("faq", "FAQ / سوالات"),
        ("privacy", "Privacy Policy / رازداری کی پالیسی"),
        ("terms", "Terms and Conditions / شرائط و ضوابط"),
        ("help", "Help / مدد"),
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES, verbose_name="Page")
    language = models.CharField(
        max_length=10, 
        choices=[("english", "English"), ("urdu", "Urdu")], 
        verbose_name="Language"
    )
    title = models.CharField(max_length=255, verbose_name="Page Title")
    content = models.TextField(verbose_name="Page Content")

    def __str__(self):
        return f"{self.get_page_display()} ({self.language.capitalize()})"
    

class ReferenceBook(models.Model):
    name_english = models.CharField(max_length=255, verbose_name="Book Name in English")
    name_urdu = models.CharField(max_length=255, verbose_name="کتاب کا نام اردو میں")

    def __str__(self):
        return self.name_english


class Keyword(models.Model):
    name_english = models.CharField(max_length=255, verbose_name="Keyword in English")
    name_urdu = models.CharField(max_length=255, verbose_name="کلیدی لفظ اردو میں")
    reference_books = models.ManyToManyField(
        ReferenceBook,
        related_name='keywords',  # This reverses the logic
        verbose_name="Associated Reference Books"
    )

    def __str__(self):
        return self.name_english

    
class Imam(models.Model):
    name_english = models.CharField(max_length=255, verbose_name="Imam Name in English")
    name_urdu = models.CharField(max_length=255, verbose_name="امام کا نام اردو میں")

    def __str__(self):
        return self.name_english
    
class Catalogue(models.Model):
    title_english = models.CharField(max_length=255, verbose_name="Catalogue Title in English")
    title_urdu = models.CharField(max_length=255, verbose_name="کیٹلاگ کا عنوان اردو میں")
    description_english = models.TextField(verbose_name="Description in English", blank=True, null=True)
    description_urdu = models.TextField(verbose_name="تفصیل اردو میں", blank=True, null=True)
    
    reference_book = models.ForeignKey(
        ReferenceBook, 
        on_delete=models.CASCADE, 
        related_name="catalogues", 
        verbose_name="Reference Book",
        blank=True, null=True
    )
    
    keyword = models.ForeignKey(
        Keyword, 
        on_delete=models.CASCADE, 
        related_name="catalogues", 
        verbose_name="Keyword",
        blank=True, null=True
    )
    
    imam = models.ForeignKey(
        Imam, 
        on_delete=models.CASCADE, 
        related_name="catalogues", 
        verbose_name="Imam",
        blank=True, null=True
    )

    def __str__(self):
        return self.title_english
    
class Index(models.Model):
    keyword = models.ForeignKey(
        Keyword,
        on_delete=models.CASCADE,
        related_name="indices",
        verbose_name="Keyword"
    )
    english_search_count = models.IntegerField(default=0, verbose_name="English Search Count")
    urdu_search_count = models.IntegerField(default=0, verbose_name="Urdu Search Count")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"Index for {self.keyword.name_english}"

    def increment_english_count(self):
        """Method to increment the English search count"""
        self.english_search_count += 1
        self.save()

    def increment_urdu_count(self):
        """Method to increment the Urdu search count"""
        self.urdu_search_count += 1
        self.save()


# class AnalyticsFilter(models.Model):
#     medium = models.CharField(max_length=255)
#     source = models.CharField(max_length=255)
    
#     sessions = models.IntegerField(default=0)
#     pageviews = models.IntegerField(default=0)
#     bounce_rate = models.FloatField(default=0.0)
    
#     date_fetched = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Source: {self.source}, Medium: {self.medium}, Sessions: {self.sessions}, Pageviews: {self.pageviews}, Bounce Rate: {self.bounce_rate}%"