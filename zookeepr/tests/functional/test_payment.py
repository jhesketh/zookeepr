from zookeepr.tests.functional import *

class TestPaymentController(ControllerTest):
    """Test that when we pump data into the payment, it does the right thing.
    """

#     def test_payment_received(self):
#         invoice = model.Invoice()
#         self.dbsession.save(invoice)
#         ii = model.InvoiceItem('foo', 1, 100)
#         self.dbsession.save(ii)
        
#         invoice.items.append(ii)

#         # do stuff

    def test_no_payment(self):
        # a random hit on the page
        
        params = dict(InvoiceID=1,
                      AuthNum=5261,
                      Amount=69001,
                      RefundKey='KJdW+tSk95x+d54+gHB1',
                      MerchantID='Test',
                      Status='Denied',
                      Settlement=1111,
                      ErrorString='x',
                      CardName='y',
                      RequestedPage='ReceiptPage1',
                      CardType='VISA',
                      MAC='0cf459a485261747bb565ec47ec434ee6fdbasdf',
                      CardNumber='51000...0009',
                      PaymentID=201,
                      TransID='SimProxy 54021550',
                      ORIGINAL_AMOUNT=69001,
                      Surcharge=1)
        resp = self.app.get('/payment/new', params=params)

        print resp

        self.fail("not really")

        # clean up
        #self.objectstore.delete(invoice)
        
