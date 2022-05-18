# Getemails Task

The Lambda function has a monolithic architecture where Forgot password and reset password HTTP endpoints are branched based on the Resource PATH and the HTTP method.
 
## Forgot Password
Case:

```If a forgot password request is made by a same user multiple times, it should generate multiple different link ```

When a new reset password link is created for the user, the previous reset password link created will be invalid and only one reset link can be valid at the given time.

## Reset Password

A separate API is created to verify if the token is valid or invalid.

### RDS
Used Amazon Aurora relational database service as it pay per use.