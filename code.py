import sentry_sdk

# Initialize Sentry
sentry_sdk.init(
    dsn="https://739a84db98165363cde37d7aed89fada@o4507498378887168.ingest.us.sentry.io/4507498385178624", 
    traces_sample_rate=1.0  
)

def divide_by_zero():
    return 1 / 0

def main():
    try:
        divide_by_zero()
    except Exception as e:
     
        sentry_sdk.capture_exception(e)
        print("Exception captured and sent to Sentry")

if _name_ == "_main_":
    main()