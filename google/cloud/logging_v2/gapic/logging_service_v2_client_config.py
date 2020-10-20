config = {
  "interfaces": {
    "google.logging.v2.LoggingServiceV2": {
      "retry_codes": {
        "retry_policy_1_codes": [
          "DEADLINE_EXCEEDED",
          "INTERNAL",
          "UNAVAILABLE"
        ],
        "no_retry_codes": [],
        "retry_policy_2_codes": [
          "DEADLINE_EXCEEDED",
          "INTERNAL",
          "UNAVAILABLE"
        ]
      },
      "retry_params": {
        "retry_policy_1_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 60000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 60000,
          "total_timeout_millis": 60000
        },
        "retry_policy_2_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 3600000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 3600000,
          "total_timeout_millis": 3600000
        },
        "no_retry_params": {
          "initial_retry_delay_millis": 0,
          "retry_delay_multiplier": 0.0,
          "max_retry_delay_millis": 0,
          "initial_rpc_timeout_millis": 0,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 0,
          "total_timeout_millis": 0
        }
      },
      "methods": {
        "DeleteLog": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params"
        },
        "ListLogEntries": {
          "timeout_millis": 10000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params"
        },
        "WriteLogEntries": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params",
          "bundling": {
            "element_count_threshold": 1000,
            "request_byte_threshold": 1048576,
            "delay_threshold_millis": 50
          }
        },
        "ListMonitoredResourceDescriptors": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params"
        },
        "ListLogs": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params"
        }
      }
    }
  }
}
