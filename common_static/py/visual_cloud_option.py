#!/usr/bin/env python3
# -*- coding: utf-8 -*-

visual_cloud = {
    'algs_info': {
        'dynamic': {
            'dm_graph_scan': {
                'name': 'dm_graph_scan',
                'elem_id': 'DMGraphScan',
                'v_name': 'DM Graph Scan',
                'desc': 'Dynamic Algorithm. DM Graph Scan visualization.',
                'visual_type': 'dynamic',
                'html': 'visual_alg.html',
                'form': {
                    'input_file': {
                        'elem_id': 'input_file',
                        'v_name': 'Input File',
                        'select': True,
                        'options': {
                            'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
                        }
                    },
                    'method': {
                        'elem_id': 'method',
                        'v_name': 'Method',
                        'type': 'number',
                        'default': 1,
                        'hidden': True
                    },
                    'alpha_max': {
                        'elem_id': 'alphaMax',
                        'v_name': 'Alpha Max',
                        'type': 'number',
                        'default': 0.15,
                    },
                    'b': {
                        'elem_id': 'b',
                        'v_name': 'B',
                        'type': 'number',
                        'default': 2,
                    },
                }
            },
            'additive_scan': {
                'name': 'additive_scan',
                'elem_id': 'additiveScan',
                'v_name': 'Additive Scan',
                'desc': 'Dynamic Algorithm.Additive Scan visualization.',
                'visual_type': 'dynamic',
                'html': 'visual_alg.html',
                'form': {
                    'input_file': {
                        'elem_id': 'input_file',
                        'v_name': 'Input File',
                        'select': True,
                        'options': {
                            'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
                        }
                    },
                    'method': {
                        'elem_id': 'method',
                        'v_name': 'Method',
                        'type': 'number',
                        'default': 3,
                        'hidden': True
                    },
                    'npss': {
                        'elem_id': 'NPSS',
                        'v_name': 'NPSS',
                        'type': 'text',
                        'default': 'BJ'
                    },
                    'iterations_bound': {
                        'elem_id': 'iterationsBound',
                        'v_name': 'Iterations Bound',
                        'type': 'number',
                        'default': 10
                    },
                    'ncores': {
                        'elem_id': 'nCores',
                        'v_name': 'N Cores',
                        'type': 'number',
                        'default': 8
                    },
                    'minutes': {
                        'elem_id': 'minutes',
                        'v_name': 'Minutes',
                        'type': 'number',
                        'default': 30
                    },
                }
            },
            'meden': {
                'name': 'meden',
                'elem_id': 'meden',
                'v_name': 'Meden',
                'desc': 'Dynamic Algorithm. Meden visualization.',
                'visual_type': 'dynamic',
                'html': 'visual_alg.html',
                'form': {
                    'input_file': {
                        'elem_id': 'input_file',
                        'v_name': 'Input File',
                        'select': True,
                        'options': {
                            'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
                        }
                    },
                    'method': {
                        'elem_id': 'method',
                        'v_name': 'Method',
                        'type': 'number',
                        'default': 5,
                        'hidden': True
                    },
                    'alpha_max': {
                        'elem_id': 'alphaMax',
                        'v_name': 'Alpha Max',
                        'type': 'number',
                        'default': 0.15
                    },
                }
            },
        },
        'static': {
            'dfs': {
                'name': 'dfs',
                'elem_id': 'DFS',
                'v_name': 'DFS',
                'desc': 'Static Algorithm. DFS visualization.',
                'visual_type': 'static',
                'html': 'visual_alg.html',
                'form': {
                    'input_file': {
                        'elem_id': 'input_file',
                        'v_name': 'Input File',
                        'select': True,
                        'options': {
                            'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
                        }
                    },
                    'method': {
                        'elem_id': 'method',
                        'v_name': 'Method',
                        'type': 'number',
                        'default': 2,
                        'hidden': True
                    },
                    'radius': {
                        'elem_id': 'radius',
                        'v_name': 'Radius',
                        'type': 'number',
                        'default': 7,
                    },
                    'anomaly_ratio': {
                        'elem_id': 'anomalyRatio',
                        'v_name': 'Anomaly Ratio',
                        'type': 'number',
                        'default': 0.5,
                    },
                    'minutes': {
                        'elem_id': 'minutes',
                        'v_name': 'Minutes',
                        'type': 'number',
                        'default': 30
                    },
                    'alpha_max': {
                        'elem_id': 'alphaMax',
                        'v_name': 'Alpha Max',
                        'type': 'number',
                        'default': 0.15
                    },
                }
            },
            'nphgs': {
                'name': 'nphgs',
                'elem_id': 'NPHGS',
                'v_name': 'NPHGS',
                'desc': 'Static Algorithm. NPHGS visualization.',
                'visual_type': 'static',
                'html': 'visual_alg.html',
                'form': {
                    'input_file': {
                        'elem_id': 'input_file',
                        'v_name': 'Input File',
                        'select': True,
                        'options': {
                            'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
                        }
                    },
                    'method': {
                        'elem_id': 'method',
                        'v_name': 'Method',
                        'type': 'number',
                        'default': 4,
                        'hidden': True
                    },
                    'alpha_max': {
                        'elem_id': 'alphaMax',
                        'v_name': 'Alpha Max',
                        'type': 'number',
                        'default': 0.15
                    },
                    'npss': {
                        'elem_id': 'NPSS',
                        'v_name': 'NPSS',
                        'type': 'text',
                        'default': 'BJ'
                    },
                }
            },
            'event_tree': {
                'name': 'event_tree',
                'elem_id': 'eventTree',
                'v_name': 'Event Tree',
                'desc': 'Static Algorithm. Event Tree visualization.',
                'visual_type': 'static',
                'html': 'visual_alg.html',
                'form': {
                    'input_file': {
                        'elem_id': 'input_file',
                        'v_name': 'Input File',
                        'select': True,
                        'options': {
                            'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
                        }
                    },
                    'method': {
                        'elem_id': 'method',
                        'v_name': 'Method',
                        'type': 'number',
                        'default': 6,
                        'hidden': True
                    },
                    'alpha_max': {
                        'elem_id': 'alphaMax',
                        'v_name': 'Alpha Max',
                        'type': 'number',
                        'default': 0.15
                    },
                }
            },
        }
    }
}

# visual_cloud = {
#     'algs_info': {
#         'graph': {
#             'dm_graph_scan': {
#                 'name': 'dm_graph_scan',
#                 'elem_id': 'DMGraphScan',
#                 'v_name': 'DM Graph Scan',
#                 'desc': 'Dynamic Algorithm. DM Graph Scan visualization.',
#                 'visual_type': 'graph',
#                 'html': 'visual_alg.html',
#                 'form': {
#                     'input_file': {
#                         'elem_id': 'input_file',
#                         'v_name': 'Input File',
#                         'select': True,
#                         'options': {
#                             'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
#                         }
#                     },
#                     'method': {
#                         'elem_id': 'method',
#                         'v_name': 'Method',
#                         'type': 'number',
#                         'default': 1,
#                         'hidden': True
#                     },
#                     'alpha_max': {
#                         'elem_id': 'alphaMax',
#                         'v_name': 'Alpha Max',
#                         'type': 'number',
#                         'default': 0.15,
#                     },
#                     'b': {
#                         'elem_id': 'b',
#                         'v_name': 'B',
#                         'type': 'number',
#                         'default': 2,
#                     },
#                 }
#             },
#             'dfs': {
#                 'name': 'dfs',
#                 'elem_id': 'DFS',
#                 'v_name': 'DFS',
#                 'desc': 'Static Algorithm. DFS visualization.',
#                 'visual_type': 'graph',
#                 'html': 'visual_alg.html',
#                 'form': {
#                     'input_file': {
#                         'elem_id': 'input_file',
#                         'v_name': 'Input File',
#                         'select': True,
#                         'options': {
#                             'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
#                         }
#                     },
#                     'method': {
#                         'elem_id': 'method',
#                         'v_name': 'Method',
#                         'type': 'number',
#                         'default': 2,
#                         'hidden': True
#                     },
#                     'radius': {
#                         'elem_id': 'radius',
#                         'v_name': 'Radius',
#                         'type': 'number',
#                         'default': 7,
#                     },
#                     'anomaly_ratio': {
#                         'elem_id': 'anomalyRatio',
#                         'v_name': 'Anomaly Ratio',
#                         'type': 'number',
#                         'default': 0.5,
#                     },
#                     'minutes': {
#                         'elem_id': 'minutes',
#                         'v_name': 'Minutes',
#                         'type': 'number',
#                         'default': 30
#                     },
#                     'alpha_max': {
#                         'elem_id': 'alphaMax',
#                         'v_name': 'Alpha Max',
#                         'type': 'number',
#                         'default': 0.15
#                     },
#                 }
#             },
#             'additive_scan': {
#                 'name': 'additive_scan',
#                 'elem_id': 'additiveScan',
#                 'v_name': 'Additive Scan',
#                 'desc': 'Dynamic Algorithm.Additive Scan visualization.',
#                 'visual_type': 'graph',
#                 'html': 'visual_alg.html',
#                 'form': {
#                     'input_file': {
#                         'elem_id': 'input_file',
#                         'v_name': 'Input File',
#                         'select': True,
#                         'options': {
#                             'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
#                         }
#                     },
#                     'method': {
#                         'elem_id': 'method',
#                         'v_name': 'Method',
#                         'type': 'number',
#                         'default': 3,
#                         'hidden': True
#                     },
#                     'npss': {
#                         'elem_id': 'NPSS',
#                         'v_name': 'NPSS',
#                         'type': 'text',
#                         'default': 'BJ'
#                     },
#                     'iterations_bound': {
#                         'elem_id': 'iterationsBound',
#                         'v_name': 'Iterations Bound',
#                         'type': 'number',
#                         'default': 10
#                     },
#                     'ncores': {
#                         'elem_id': 'nCores',
#                         'v_name': 'N Cores',
#                         'type': 'number',
#                         'default': 8
#                     },
#                     'minutes': {
#                         'elem_id': 'minutes',
#                         'v_name': 'Minutes',
#                         'type': 'number',
#                         'default': 30
#                     },
#                 }
#             },
#             'nphgs': {
#                 'name': 'nphgs',
#                 'elem_id': 'NPHGS',
#                 'v_name': 'NPHGS',
#                 'desc': 'Static Algorithm. NPHGS visualization.',
#                 'visual_type': 'graph',
#                 'html': 'visual_alg.html',
#                 'form': {
#                     'input_file': {
#                         'elem_id': 'input_file',
#                         'v_name': 'Input File',
#                         'select': True,
#                         'options': {
#                             'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
#                         }
#                     },
#                     'method': {
#                         'elem_id': 'method',
#                         'v_name': 'Method',
#                         'type': 'number',
#                         'default': 4,
#                         'hidden': True
#                     },
#                     'alpha_max': {
#                         'elem_id': 'alphaMax',
#                         'v_name': 'Alpha Max',
#                         'type': 'number',
#                         'default': 0.15
#                     },
#                     'npss': {
#                         'elem_id': 'NPSS',
#                         'v_name': 'NPSS',
#                         'type': 'text',
#                         'default': 'BJ'
#                     },
#                 }
#             },
#             'meden': {
#                 'name': 'meden',
#                 'elem_id': 'meden',
#                 'v_name': 'Meden',
#                 'desc': 'Dynamic Algorithm. Meden visualization.',
#                 'visual_type': 'graph',
#                 'html': 'visual_alg.html',
#                 'form': {
#                     'input_file': {
#                         'elem_id': 'input_file',
#                         'v_name': 'Input File',
#                         'select': True,
#                         'options': {
#                             'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
#                         }
#                     },
#                     'method': {
#                         'elem_id': 'method',
#                         'v_name': 'Method',
#                         'type': 'number',
#                         'default': 5,
#                         'hidden': True
#                     },
#                     'alpha_max': {
#                         'elem_id': 'alphaMax',
#                         'v_name': 'Alpha Max',
#                         'type': 'number',
#                         'default': 0.15
#                     },
#                 }
#             },
#             'event_tree': {
#                 'name': 'event_tree',
#                 'elem_id': 'eventTree',
#                 'v_name': 'Event Tree',
#                 'desc': 'Static Algorithm. Event Tree visualization.',
#                 'visual_type': 'graph',
#                 'html': 'visual_alg.html',
#                 'form': {
#                     'input_file': {
#                         'elem_id': 'input_file',
#                         'v_name': 'Input File',
#                         'select': True,
#                         'options': {
#                             'Graph.json': './visualization/alg_scripts/MGraph/Graph.json'
#                         }
#                     },
#                     'method': {
#                         'elem_id': 'method',
#                         'v_name': 'Method',
#                         'type': 'number',
#                         'default': 6,
#                         'hidden': True
#                     },
#                     'alpha_max': {
#                         'elem_id': 'alphaMax',
#                         'v_name': 'Alpha Max',
#                         'type': 'number',
#                         'default': 0.15
#                     },
#                 }
#             },
#         },
#     }
# }