mails={
    
    "Login":f'<h1 style=\'color: #333; text-align: center;\'>New Login Notification</h1><p style=\'color: #555; text-align: center; max-width: 600px; margin: 0 auto;\'>Dear <b style=\'color: #3498db;\'>{{name}}</b>,</p><div style=\'background-color: #fff; border-radius: 5px; padding: 20px; margin-top: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);\'><p style=\'color: #555;\'>We hope this message finds you well. There was a new login to your account at <b style=\'color: #3498db;\'>{{time_string}}</b>. If this was you, no further action is required.</p></div><p style=\'color: #888; text-align: center; margin-top: 20px;\'>Thank you for choosing our service.</p><p style=\'color: #555; text-align: center;\'>Best regards,</p><p style=\'color: #555; text-align: center;\'>A2 Industries</p>',
    
    "Logout":f'<h1 style=\'color: #333; text-align: center;\'>New Logout Notification</h1><p style=\'color: #555; text-align: center; max-width: 600px; margin: 0 auto;\'>Dear <b style=\'color: #3498db;\'>{{name}}</b>,</p><div style=\'background-color: #fff; border-radius: 5px; padding: 20px; margin-top: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);\'><p style=\'color: #555;\'>We hope this message finds you well. There was a new logout to your account at <b style=\'color: #3498db;\'>{{time_string}}</b>. If this was you, no further action is required.</p></div><p style=\'color: #888; text-align: center; margin-top: 20px;\'>Thank you for choosing our service.</p><p style=\'color: #555; text-align: center;\'>Best regards,</p><p style=\'color: #555; text-align: center;\'>A2 Industries</p>',
    
    "Taskassignedstaff":f"Hey <b style='color: #3498db; font-size: 18px;'>{{namestaff}}</b>,<div style='margin-top: 10px;'><p style='color: #555; font-size: 16px;'>You have a new task assigned at <b>{{time_string}}</b>.</p><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Task Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Task ID:</b> {{taskid}}</li><li><b style='color: #3498db;'>Task Name:</b> {{taskname}}</li><li><b style='color: #3498db;'>Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li></ul></div></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p>",

    "Taskassignedmanager":f"Hey <b style='color: #3498db; font-size: 18px;'>{{namemanager}}</b>,<div style='margin-top: 10px;'><p style='color: #555; font-size: 16px;'>You assigned a new task at <b>{{time_string}} to {{namestaff}}</b>.</p><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Task Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Task ID:</b> {{taskid}}</li><li><b style='color: #3498db;'>Task Name:</b> {{taskname}}</li><li><b style='color: #3498db;'>Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li></ul></div></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p>",
    
    "Updatetaskstatusstaff":f"Hey {{namestaff}}, your request for task approval is submitted to {{repmanager}} at {{time_string}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Task Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Task ID:</b> {{taskid}}</li><li><b style='color: #3498db;'>Task Name:</b> {{taskname}}</li><li><b style='color: #3498db;'>Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Added Notes:</b> {{addnotes}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p>",

    "Updatetaskstatusmanager":f"Hey {{namemanager}}, your recived a request for task approval at {{time_string}} by {{namestaff}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Task Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Task ID:</b> {{taskid}}</li><li><b style='color: #3498db;'>Task Name:</b> {{taskname}}</li><li><b style='color: #3498db;'>Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Added Notes:</b> {{addnotes}}</li><li><b style='color: #3498db;'>Updated Status:</b> {{status}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p>",

    "Leaverequeststaff":f"Hey {{namestaff}}, your request for leave is submitted to {{repmanager}} at {{time_string}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Leave Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Leave ID:</b> {{leaveid}}</li><li><b style='color: #3498db;'>Leave Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>Leave End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Leave Type:</b> {{typeofleave}}</li><li><b style='color: #3498db;'>Leave Duration:</b> {{leaveduration}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p>",

    "Leaverequestmanager":f"Hey {{namemanager}}, {{namestaff}} requested for leave at {{time_string}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Leave Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Leave ID:</b> {{leaveid}}</li><li><b style='color: #3498db;'>Leave Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>Leave End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Leave Type:</b> {{typeofleave}}</li><li><b style='color: #3498db;'>Leave Duration:</b> {{leaveduration}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p>",

    "Taskapprovalstaff":f"Hey {{namestaff}}, your request for approval of task is modified by {{username}} at {{time_string}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Task Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Task ID:</b> {{taskid}}</li><li><b style='color: #3498db;'>Task Name:</b> {{taskname}}</li><li><b style='color: #3498db;'>Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Added Notes:</b> {{addnotes}}</li><li><b style='color: #3498db;'>Requested Status:</b> {{status}}</li><li><b style='color: #3498db;'>Approval Status:</b> {{approvalstatus}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p><p style='color: #888; font-size: 14px; margin-top: 10px;'>We're pleased to inform you that your task approval request has been successfully approved. This is an automated message to let you know about the status of your task approval. If you have any further questions or concerns, feel free to reach out to our support team.</p><p style='color: #555; font-size: 14px;'>Best regards,</p></p><p style='color: #555; font-size: 14px;'>A2 Entreprises</p>",
    
    "Taskapprovalmanager":f"Hey {{namemanager}}, you modified request for approval of task of {{namestaff}} at {{time_string}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Task Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Task ID:</b> {{taskid}}</li><li><b style='color: #3498db;'>Task Name:</b> {{taskname}}</li><li><b style='color: #3498db;'>Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Added Notes:</b> {{addnotes}}</li><li><b style='color: #3498db;'>Requested Status:</b> {{status}}</li><li><b style='color: #3498db;'>Approval Status:</b> {{approvalstatus}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p><p style='color: #888; font-size: 14px; margin-top: 10px;'>We're pleased to inform you that your task approval request has been successfully approved. This is an automated message to let you know about the status of your task approval. If you have any further questions or concerns, feel free to reach out to our support team.</p><p style='color: #555; font-size: 14px;'>Best regards,</p></p><p style='color: #555; font-size: 14px;'>A2 Entreprises</p>",

    "Leaveapprovalstaff":f"Hey {{namestaff}}, your leave request is modified by {{username}} at {{time_string}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Leave Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Leave ID:</b> {{leaveid}}</li><li><b style='color: #3498db;'>Leave Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>Leave End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Leave Duration:</b> {{leaveduration}}</li><li><b style='color: #3498db;'>Requested Date:</b> {{requestdate}}</li><li><b style='color: #3498db;'>Approval Status:</b> {{approvalstatus}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p><p style='color: #888; font-size: 14px; margin-top: 10px;'>We're pleased to inform you that your leave request has been successfully modified. This is an automated message to let you know about the status of your leave approval. If you have any further questions or concerns, feel free to reach out to our support team.</p><p style='color: #555; font-size: 14px;'>Best regards,</p><p style='color: #555; font-size: 14px;'>A2 Enterprises</p>",
    
    "Leaveapprovalmanager":f"Hey {{namemanager}}, you modified leave request of {{namestaff}} {{empid}} at {{time_string}}<br><div style='background-color: #f7f7f7; border-radius: 5px; padding: 15px; margin-top: 10px;'><p style='color: #333; font-size: 16px;'>Leave Details:</p><ul style='list-style-type: none; padding: 0; margin: 0;'><li><b style='color: #3498db;'>Leave ID:</b> {{leaveid}}</li><li><b style='color: #3498db;'>Leave Start Date:</b> {{startdate}}</li><li><b style='color: #3498db;'>Leave End Date:</b> {{enddate}}</li><li><b style='color: #3498db;'>Notes:</b> {{notes}}</li><li><b style='color: #3498db;'>Leave Duration:</b> {{leaveduration}}</li><li><b style='color: #3498db;'>Requested Date:</b> {{requestdate}}</li><li><b style='color: #3498db;'>Approval Status:</b> {{approvalstatus}}</li></ul></div><p style='color: #555; font-size: 16px; margin-top: 10px;'>Thank You</p><p style='color: #888; font-size: 14px; margin-top: 10px;'>We're pleased to inform you that your leave request has been successfully approved. This is an automated message to let you know about the status of  leave approval. If you have any further questions or concerns, feel free to reach out to our support team.</p><p style='color: #555; font-size: 14px;'>Best regards,</p><p style='color: #555; font-size: 14px;'>A2 Enterprises</p>",

    "Taskdetailsupdatestaff":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Notification of Task Details Update</p><p style=\"font-size: 16px;\">Hello <span style=\"color: #007bff;\">{{namestaff}}</span>,</p><p style=\"font-size: 16px;\">The details for the task named <span style=\"font-weight: bold; color: #007bff;\">{{taskname1}}</span> have been updated by <span style=\"font-weight: bold; color: #007bff;\">{{username}}</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span>.</p><ul style=\"list-style-type: none; padding: 0; margin: 0;\"><li><strong>Task ID:</strong> {{taskid}}</li><li><strong>Task Name:</strong> {{taskname2}}</li><li><strong>Task Start Date:</strong> {{startdate}}</li><li><strong>Task End Date:</strong> {{enddate}}</li><li><strong>Notes:</strong> {{notes}}</li><li><strong>Status:</strong> {{status}}</li></ul><p style=\"font-size: 16px;\">Thank you for your attention and cooperation.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",

    "Taskdetailsupdatemanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Task Details Update Notification</p><p style=\"font-size: 16px;\">Hey <span style=\"font-weight: bold; color: #007bff;\">{{namemanager}}</span>,</p><p style=\"font-size: 16px;\">You have updated the details for the task named <span style=\"font-weight: bold; color: #007bff;\">{{taskname1}}</span> assigned to <span style=\"font-weight: bold; color: #007bff;\">{{namestaff}} ({{empid}})</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span>.</p><ul style=\"list-style-type: none; padding: 0; margin: 0;\"><li><strong>Task ID:</strong> {{taskid}}</li><li><strong>Task Name:</strong> {{taskname2}}</li><li><strong>Task Start Date:</strong> {{startdate}}</li><li><strong>Task End Date:</strong> {{enddate}}</li><li><strong>Notes:</strong> {{notes}}</li><li><strong>Status:</strong> {{status}}</li></ul><p style=\"font-size: 16px;\">Thank you for your attention and cooperation.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",
    
    "Pullrequestcurrentmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Pull Request Notification</p><p style=\"font-size: 16px;\"><b>Hey <span style=\"font-weight: bold; color: #007bff;\">{{name}}</span>, you received a pull request by <span style=\"font-weight: bold; color: #007bff;\">{{requestingmanager1}}</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span></b></p><p style=\"font-size: 16px;\">Resource: <span style=\"font-weight: bold; color: #007bff;\">{{empid}}</span><br>Requesting Person: <span style=\"font-weight: bold; color: #007bff;\">{{requestingmanager2}}</span></p><p style=\"font-size: 16px;\">Thank you for your attention.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",
    
    "Pullrequestreportingmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Pull Request Notification</p><p style=\"font-size: 16px;\"><b>Hey <span style=\"font-weight: bold; color: #007bff;\">{{name}}</span>, you requested a pull request to <span style=\"font-weight: bold; color: #007bff;\">{{currentrepmanager1}}</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span></b></p><p style=\"font-size: 16px;\">Resource: <span style=\"font-weight: bold; color: #007bff;\">{{empid}}</span><br>Requested Person: <span style=\"font-weight: bold; color: #007bff;\">{{currentrepmanager2}}</span></p><p style=\"font-size: 16px;\">Thank you for your attention.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",

    "Pullrequestapprcurrmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Pull Request Approval Notification</p><p style=\"font-size: 16px;\"><b>Hey <span style=\"font-weight: bold; color: #007bff;\">{{name}}</span>, you approved a pull request of <span style=\"font-weight: bold; color: #007bff;\">{{empid1}}</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span></b></p><p style=\"font-size: 16px;\">Resource: <span style=\"font-weight: bold; color: #007bff;\">{{empid2}}</span><br>Requesting Person: <span style=\"font-weight: bold; color: #007bff;\">{{requestingmanager}}</span><br>Request Date: <span style=\"font-weight: bold; color: #007bff;\">{{requestdate}}</span></p><p style=\"font-size: 16px;\">Thank you for your approval.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",
    
    "Pullrequestapprrepmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Pull Request Approval Notification</p><p style=\"font-size: 16px;\"><b>Hey <span style=\"font-weight: bold; color: #007bff;\">{{name}}</span>, the pull request of <span style=\"font-weight: bold; color: #007bff;\">{{empid1}}</span> is approved by <span style=\"font-weight: bold; color: #007bff;\">{{username1}}</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span></b></p><p style=\"font-size: 16px;\">Resource: <span style=\"font-weight: bold; color: #007bff;\">{{empid2}}</span><br>Requested Person: <span style=\"font-weight: bold; color: #007bff;\">{{username2}}</span><br>Request Date: <span style=\"font-weight: bold; color: #007bff;\">{{requestdate}}</span><br>Approval Status: <span style=\"font-weight: bold; color: #007bff;\">Approved</span></p><p style=\"font-size: 16px;\">Thank you for your approval.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",
    
    "Pullrequestemp":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Manager Change Notification</p><p style=\"font-size: 16px;\"><b>Hey <span style=\"font-weight: bold; color: #007bff;\">{{name}}</span>, your manager is changed from <span style=\"font-weight: bold; color: #007bff;\">{{username}}</span> to <span style=\"font-weight: bold; color: #007bff;\">{{requestingmanager}}</span>.</b></p><p style=\"font-size: 16px;\">Kindly contact your new manager. Your reporting manager would assign tasks to you if required.</p><p style=\"font-size: 14px; color: #888;\">Thank you</p></div>",

    "Pullreqcurrmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Pull Request Rejected Notification</p><p style=\"font-size: 16px;\"><b>Hey <span style=\"font-weight: bold; color: #007bff;\">{{name}}</span>, you rejected a pull request of <span style=\"font-weight: bold; color: #007bff;\">{{empid1}}</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span></b></p><p style=\"font-size: 16px;\">Resource: <span style=\"font-weight: bold; color: #007bff;\">{{empid2}}</span><br>Requesting Person: <span style=\"font-weight: bold; color: #007bff;\">{{requestingmanager}}</span><br>Request Date: <span style=\"font-weight: bold; color: #007bff;\">{{requestdate}}</span></p><p style=\"font-size: 16px;\">Thank you for your approval.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",

    "Pullreqrepmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><p style=\"font-size: 18px; font-weight: bold; color: #007bff;\">Pull Request Disapproval Notification</p><p style=\"font-size: 16px;\"><b>Hey <span style=\"font-weight: bold; color: #007bff;\">{{name}}</span>, the pull request of <span style=\"font-weight: bold; color: #007bff;\">{{empid1}}</span> is rejected by <span style=\"font-weight: bold; color: #007bff;\">{{username1}}</span> at <span style=\"font-weight: bold; color: #007bff;\">{{time_string}}</span></b></p><p style=\"font-size: 16px;\">Resource: <span style=\"font-weight: bold; color: #007bff;\">{{empid2}}</span><br>Requested Person: <span style=\"font-weight: bold; color: #007bff;\">{{username2}}</span><br>Request Date: <span style=\"font-weight: bold; color: #007bff;\">{{requestdate}}</span><br>Approval Status: <span style=\"font-weight: bold; color: #007bff;\">Disapproved</span></p><p style=\"font-size: 16px;\">Thank you for your approval.</p><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",

    "Acccreatedstaff":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><h3>Hi <span style=\"font-weight: bold; color: #007bff;\">{{namestaff}}</span></h3><br><b>Welcome To A2.</b><br><p style='color:red'>Congratulations <span style=\"font-weight: bold; color: #007bff;\">{{namestaff}}</span>, your profile is successfully created in our databases.<br>Your loginid would be <b>{{empid}}</b><br>Password would be your date of birth in format <b>YYYY-MM-DD</b><br>Note: Remember to change your password to a secured one.<br>Once again welcome to A2<br>Thank You</p><a href='http://127.0.0.1:5001/'>Click here to SignIn</a></div>",

    "Acccreatedmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><h3>Hi <span style=\"font-weight: bold; color: #007bff;\">{{nameadmin}}</span></h3><br><p style='color:red'>Account creation of <span style=\"font-weight: bold; color: #007bff;\">{{namestaff}}</span> with empid <b>{{empid}}</b> is done.<br>Thank You</p></div>",
    
    "Repmanager":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><h3>Hi <span style=\"font-weight: bold; color: #007bff;\">{{namerepmanager}}</span><br><span style=\" color: #007bff;\">It is to inform you that {{namestaff}} {{empid}} is removed from your reporting persons</span><br><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",
    
    "Staff":f"<div style=\"font-family: 'Helvetica Neue', Arial, sans-serif; color: #555; max-width: 600px; margin: 0 auto;\"><h3>Hi <span style=\"font-weight: bold; color: #007bff;\">{{namestaff}}</span><br><span style=\" color: #007bff;\">It is to inform you that {{namestaff}} {{empid}} is removed from our databases effective from {{effectivedate}}.<br>Reason for removal: {{reason}}. You can't apply to A2 Pvt Ltd. till 6 months from effective date.<br>Thanks</span><br><p style=\"font-size: 14px; color: #888;\">This is an automated message. Please do not reply.</p></div>",
    
    "Passchanged":f"<p style='font-family: Helvetica Neue, Arial, sans-serif; font-size: 16px; color: #333; line-height: 1.6;'><b>Hello {{namestaff}},</b><br>Your password for employee ID <b>{{empid}}</b> has been successfully changed at <b>{{time_string}}</b>. This ensures the security of your account.<br>If you did not make this change or have any concerns, please contact our support team immediately.<br>Thank you for keeping your account secure!<br><br><i>This is an automated message. Please do not reply.</i></p>"



}
