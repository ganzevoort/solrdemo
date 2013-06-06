from django.http import HttpResponse
from django.template import loader, RequestContext
from django import forms
import simplejson as json
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView
from haystack.forms import FacetedSearchForm


def autocomplete(request):
    partial = request.REQUEST.get('q', '')
    sqs = SearchQuerySet().autocomplete(content_auto=partial)[:5]
    suggestions = [str(result.object) for result in sqs]
    results = json.dumps({'results': suggestions})
    return HttpResponse(results, content_type='application/json')


class CarsSearchForm(FacetedSearchForm):
    max_milage = forms.IntegerField(required=False)

    def search(self):
        sqs = super(CarsSearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()
        if self.cleaned_data['max_milage']:
            sqs = sqs.filter(milage__lte=self.cleaned_data['max_milage'])
        return sqs


class CarsSearchView(FacetedSearchView):
    def __init__(self, *args, **kwargs):
        kwargs['searchqueryset'] = SearchQuerySet().facet('milage')
        kwargs['form_class'] = CarsSearchForm
        super(CarsSearchView, self).__init__(*args, **kwargs)


def homepage(request):
    t = loader.get_template('homepage.html')
    context = RequestContext(request)
    return HttpResponse(t.render(context))

