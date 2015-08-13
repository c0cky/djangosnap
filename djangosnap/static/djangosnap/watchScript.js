(function(jQuery) {
  // saveAll dirty models in a collection. Uses jQuery when/then to chain
    // http://stackoverflow.com/questions/5014216/
    //     best-practice-for-saving-an-entire-collection
    Backbone.Collection.prototype.saveAll = function(options) {
        return jQuery.when.apply(jQuery, _.map(this.models, function(m) {
           return m.save({}, {wait: true, async: false}).then(_.identity);
        }));
    };

    var Media = Backbone.Model.extend({
        urlRoot: '/api/media/',
        toTemplate: function() {
            return _(this.attributes).clone();
        },
        addUpvote: function() {
            return this.get('up_vote')++;
        },
        addDownvote: function() {
            return this.get('down_vote')++;
        },
        getTotalPoints: function() {
            return this.get('up_vote') - this.get('down_vote');
        } 
    });

    var MediaList = Backbone.Collection.extend({
        urlRoot: '/api/media/',
        model: Media,
        comparator: function(obj) {
            return obj.get("upload_time");
        },
        toTemplate: function() {
            var a = [];
            this.forEach(function(item) {
                a.push(item.toTemplate());
            });
            return a;
        },
        getByDataId: function(id) {
            var internalId = this.urlRoot + id + '/';
            return this.get(internalId);
        },
        getByRegion: function(region) {
            return this.find(function(term) {
                return term.get("region") === region;
            });
        }
    });

    var Vocabulary = Backbone.Model.extend({
        urlRoot: '/api/vocabulary/',
        parse: function(response) {
            if (response) {
                response.term_set = new TermList(response.term_set);
            }

            return response;
        },
        toTemplate: function() {
            var json = _(this.attributes).clone();
            json.term_set = this.get('term_set').toTemplate();
            return json;
        },
        getOnomyUrls: function() {
            // the onomy url field was conceived as a comma-delimited list
            // of urls. reconstitute as an array here for easier searching
            // and adding new urls
            var urls = [];
            var str = this.get('onomy_url');
            if (str.length > 0) {
                urls = str.split(',');
            }
            return urls;
        },
        hasTerm: function(termName) {
            return this.get('term_set').getByDisplayName(termName);
        },
        addTerm: function(termName, uri) {
            if (!this.hasTerm(termName)) {
                var term = new Term({display_name: termName, skos_uri: uri});
                this.get('term_set').add(term);
            }
        }
    });

    var VocabularyList = Backbone.Collection.extend({
        urlRoot: '/api/vocabulary/',
        model: Vocabulary,
        comparator: function(obj) {
            return obj.get("display_name");
        },
        parse: function(response) {
            return response.objects || response;
        },
        toTemplate: function() {
            var a = [];
            this.forEach(function(item) {
                a.push(item.toTemplate());
            });
            return a;
        },
        getByDataId: function(id) {
            var internalId = this.urlRoot + id + '/';
            return this.get(internalId);
        },
        getByDisplayName: function(displayName) {
            return this.find(function(vocab) {
                return vocab.get("display_name") === displayName;
            });
        }
    });


}(jQuery));