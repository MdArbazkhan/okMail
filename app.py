from flask import Flask, jsonify, request,redirect
from rmq.send_rmq import publish_to_queue
import json
import validators

publisher = Flask(__name__)

@publisher.route('/test')
def home():
    return jsonify(message='Looking good'), 200


@publisher.route('/mail/<business_mail>/<path:custom_page>', methods = ['GET'])
def http_route(business_mail,custom_page="None"):
    request_data = request.args.to_dict()
    print(custom_page)
    data = {'request_data':request_data, 'business_mail':business_mail}
    # publish to queue
    # serialize the dictionary into strings then send them over RabbitMQ
    data=json.dumps(data)
    print(len(custom_page), ' : custom_page size')
    publish_to_queue('mail_queue','',data,'')
    # if not a valid url then forward to default thank you page
    if not validators.url(custom_page):
        return redirect('https://google.com')
    return redirect(custom_page)


if __name__ == '__main__':
    publisher.run(debug=True, port=8080)