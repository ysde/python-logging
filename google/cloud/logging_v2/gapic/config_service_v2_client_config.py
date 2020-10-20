config = {
  "interfaces": {
    "google.logging.v2.ConfigServiceV2": {
      "retry_codes": {
        "no_retry_2_codes": [],
        "no_retry_codes": [],
        "retry_policy_3_codes": [
          "DEADLINE_EXCEEDED",
          "INTERNAL",
          "UNAVAILABLE"
        ]
      },
      "retry_params": {
        "retry_policy_3_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 60000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 60000,
          "total_timeout_millis": 60000
        },
        "no_retry_params": {
          "initial_retry_delay_millis": 0,
          "retry_delay_multiplier": 0.0,
          "max_retry_delay_millis": 0,
          "initial_rpc_timeout_millis": 0,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 0,
          "total_timeout_millis": 0
        },
        "no_retry_2_params": {
          "initial_retry_delay_millis": 0,
          "retry_delay_multiplier": 0.0,
          "max_retry_delay_millis": 0,
          "initial_rpc_timeout_millis": 120000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 120000,
          "total_timeout_millis": 120000
        }
      },
      "methods": {
        "DeleteSink": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_3_codes",
          "retry_params_name": "retry_policy_3_params"
        },
        "UpdateSink": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_3_codes",
          "retry_params_name": "retry_policy_3_params"
        },
        "DeleteExclusion": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_3_codes",
          "retry_params_name": "retry_policy_3_params"
        },
        "ListBuckets": {
          "timeout_millis": 60000,
          "retry_codes_name": "no_retry_codes",
          "retry_params_name": "no_retry_params"
        },
        "GetBucket": {
          "timeout_millis": 60000,
          "retry_codes_name": "no_retry_codes",
          "retry_params_name": "no_retry_params"
        },
        "UpdateBucket": {
          "timeout_millis": 60000,
          "retry_codes_name": "no_retry_codes",
          "retry_params_name": "no_retry_params"
        },
        "ListSinks": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_3_codes",
          "retry_params_name": "retry_policy_3_params"
        },
        "GetSink": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_3_codes",
          "retry_params_name": "retry_policy_3_params"
        },
        "CreateSink": {
          "timeout_millis": 120000,
          "retry_codes_name": "no_retry_2_codes",
          "retry_params_name": "no_retry_2_params"
        },
        "ListExclusions": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_3_codes",
          "retry_params_name": "retry_policy_3_params"
        },
        "GetExclusion": {
          "timeout_millis": 60000,
          "retry_codes_name": "retry_policy_3_codes",
          "retry_params_name": "retry_policy_3_params"
        },
        "CreateExclusion": {
          "timeout_millis": 120000,
          "retry_codes_name": "no_retry_2_codes",
          "retry_params_name": "no_retry_2_params"
        },
        "UpdateExclusion": {
          "timeout_millis": 120000,
          "retry_codes_name": "no_retry_2_codes",
          "retry_params_name": "no_retry_2_params"
        },
        "GetCmekSettings": {
          "timeout_millis": 60000,
          "retry_codes_name": "no_retry_codes",
          "retry_params_name": "no_retry_params"
        },
        "UpdateCmekSettings": {
          "timeout_millis": 60000,
          "retry_codes_name": "no_retry_codes",
          "retry_params_name": "no_retry_params"
        }
      }
    }
  }
}
