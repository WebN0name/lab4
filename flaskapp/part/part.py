from flask_restplus import Namespace, Resource, fields
api = Namespace('part', description='some information')

info = api.model('part', {
    'id': fields.String(required=True, description='The identifier'),
    'name': fields.String(required=True, description='The name'),
})

INFO = [    {'id': '1111', 'name': 'Alex'},]

@api.route('/')

class InfoList(Resource):
    @api.marshal_list_with(info)
    def get(self):
        '''List all / это описание появится в браузере на экране напротив get'''
        return INFO

@api.route('/<id>')
@api.param('id', 'The identifier')
@api.response(404, 'id not found')
class InfoId(Resource):
    @api.doc(params={'id': 'An ID'}) # описание id в документации по адресу 127.0.0.1 
    @api.marshal_with(info)
    def get(self, id):
        for idi in INFO:            
            if idi['id'] == id:                
                return idi
            else:            
                return {'id': id, 'name': 'your name'},
            api.abort(404)