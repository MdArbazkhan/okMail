## okMail
# Get your form response directly to your email inbox
####  Use your own front-end code. Submit to our API. Set a custom thank you page. 

```
<form action="http://okmail.cloud/mail/{your_email}/{url_to_custom_thank_you_page}" method="GET">
  <label for="email">Your Email</label>
  <input name="Customer email" id="email" type="email">
	<label for="name">Your Name</label>
  <input name="Customer name" id="name" type="name">
  <button type="submit">Submit</button>
</form>
```

## Setup in 3 easy steps
##### 1. Create a correct end point with `{your_email}` and url for `custom_thank_you_page`. If you want [defualt thank_you_page](http://) then set `NaN` for the `{url_to_custom_thank_you_page}`.

#### 2. Submit first sample contact form and wait for the message to appear in your inbox from `okMail`.
#### 3. If all good, Now enjoy serverless!! 
## API End Point Example
#### 1. API End point with *default* thank you page
`http://okmail.cloud/mail/customer@frozenspoon.com/NaN`
#### 2. API End point with *custom* thank you page
`http://okmail.cloud/mail/customer@frozenspoon.com/https://frozenspoon.com/thankyou`

## Contact Us
Reach out to me via email @ `arbazkhan2772@gmail.com`
