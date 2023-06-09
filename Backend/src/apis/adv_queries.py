import db
from flask import request
from flask_restx import Namespace, Resource

ns = Namespace('adv_query', description='Advance Query')

get_sport_stats_parser = ns.parser()
get_sport_stats_parser.add_argument('sport_id', type=int, required=True, default=-1)
get_sport_stats_parser.add_argument('start_date', type=str, required=True, default='')
get_sport_stats_parser.add_argument('end_date', type=str, required=True, default='')

@ns.route('/sport_statistics')
class Q1(Resource):
    @ns.expect(get_sport_stats_parser)
    def get(self):
        sport_stats_data = get_sport_stats_parser.parse_args(strict=True)
        if sport_stats_data.get('sport_id', -1) == -1:
            return {'message': 'Please provide sport_id'}, 400
        if sport_stats_data.get('start_date', '') == '':
            return {'message': 'Please provide start_date'}, 400
        if sport_stats_data.get('end_date', '') == '':
            return {'message': 'Please provide end_date'}, 400
        result, error_msg, ret_code = db.get_sport_statistics(sport_stats_data.get('sport_id', -1), sport_stats_data.get('start_date', ''), sport_stats_data.get('end_date', ''))
        if error_msg is not None:
            return {'message': error_msg}, ret_code
        return result, ret_code


@ns.route('/profitable_events')
class Q2(Resource):
    def get(self):
        data, error_msg, ret_code = db.get_profitable_events_by_revenue()
        if error_msg:
            return {'error': error_msg}, ret_code
        return data, ret_code


@ns.route(('/get_user_kundali/<string:net_id>'))
class Q3(Resource):
    def get(self, net_id = None):
        if net_id is None: return None, 400
        data, error_msg, ret_code = db.get_user_kundali(net_id.lower())
        if error_msg:
            return {'error': error_msg}, ret_code
        return data, ret_code

@ns.route('/get_total_revenue')
class Q4(Resource):
    def get(self):
        data, error_msg, ret_code = db.get_total_revenue()
        if error_msg:
            return {'error': error_msg}, ret_code
        return data[0], ret_code

@ns.route('/get_total_bookings')
class Q5(Resource):
    def get(self):
        data, error_msg, ret_code = db.get_total_bookings()
        if error_msg:
            return {'error': error_msg}, ret_code
        return data[0], ret_code

# ## Bookings by Week day
@ns.route('bookings_by_weekday')
class Q6(Resource):
    def get(self):
        data, error_msg, ret_code = db.get_bookings_by_weekday()
        if error_msg:
            return {'error': error_msg}, ret_code
        return data, ret_code

@ns.route('/get_total_events_and_tickets_sold')
class Q7(Resource):
    def get(self):
        data, error_msg, ret_code = db.get_total_events_and_tickets_sold()
        if error_msg:
            return {'error': error_msg}, ret_code
        return data[0], ret_code

@ns.route('/get_tickets_sold_per_event')
class Q8(Resource):
    def get(self):
        data, error_msg, ret_code = db.get_tickets_sold_per_event()
        if error_msg:
            return {'error': error_msg}, ret_code
        return data, ret_code
