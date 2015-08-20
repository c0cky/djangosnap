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

    window.MediaListView = Backbone.View.extend({
        // events: {
        //     'click a.up-vote' : 'up-vote',
        //     'click a.down-vote' : 'down-vote'
        // },
        initialize: function(options) {
            // _.bindAll(this, "up-vote", "down-vote");
            _.bindAll(this, "render");
            this.context = options;
            this.medialistTemplate =
                _.template(jQuery("#watch-template").html());

            this.collection = new MediaList();
            this.collection.on("add", this.render);
            this.collection.on("remove", this.render);
            this.collection.on("reset", this.render);
            this.collection.on("sync", this.render);
            this.collection.fetch();
        },
        render: function() {
            this.context.mediafiles = this.collection.toTemplate();
            var markup = this.medialistTemplate(this.context);
            jQuery(this.el).html(markup);
        }

    });


}(jQuery));