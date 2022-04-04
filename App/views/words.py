from App.controllers import (
    get_all_words
)

word_views = Blueprint('word_views', __name__, template_folder='../templates')

# @word_views.route('/loadwords')
# def load():
#     get_all_words()
#     form=signup_button()
#     return render_template('index.html', form=form)