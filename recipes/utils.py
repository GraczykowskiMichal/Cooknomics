from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse


# Paginates the data
def do_pagination(data, number_of_pages, page_number):
    paginator = Paginator(data, number_of_pages)
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        raise Http404

    # If there are no recipes, return 404 (internet says so)
    if len(data) == 0:
        raise Http404

    page_data = {'objects': []}

    for r in page.object_list:
        recipe_dict = model_to_dict(r, exclude=['published_date',
                                              'image',
                                              'ingredients'
                                                ])
        recipe_dict['slug'] = r.slug
        recipe_dict['image_url'] = r.image.url
        recipe_dict['published_date'] = r.published_date.timestamp()
        recipe_dict['url'] = \
            reverse('recipes:recipe', kwargs={'recipe_slug': r.slug})
        page_data['objects'].append(recipe_dict)

    page_data['has_next'] = page.has_next()

    context = {
        "page": page_data
    }

    return context