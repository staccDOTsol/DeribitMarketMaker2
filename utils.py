from collections import OrderedDict

import logging, math, random

def append_comma( x ):
    return str( x ) + ', '

def append_to_output( op, listargs ):
    if op is None or len( op ) == 0:
        op = append_comma( listargs[ 0 ] ); listargs = listargs[ 1 : ]
    for x in listargs:
        op += append_comma( x )
    return op
    
    
def clamp( x, lower, upper ):
    return max( lower, min( x, upper ))


def get_logger( name, log_level ):

    formatter = logging.Formatter(
        fmt = '%(asctime)s - %(levelname)s - %(message)s' )

    handler = logging.StreamHandler()
    
    handler.setFormatter( formatter )

    logger = logging.getLogger( name )
    
    logger.setLevel( log_level )
    logger.addHandler( handler )
    
    return logger


def lag( ch, n ):
    return 'L' + str( n ) + ch

def print_dict( dictarg, 
                multiple            = 1, 
                roundto             = 0, 
                title               = None, 
                linebreak_before    = True,
                linebreak_after     = False ):
    
    d = { k: round( multiple * v, roundto ) if v is not None and type( v ) != str
         else v for k, v in dictarg.items() }
    
    if roundto == 0:
        d = { k: int( v ) if v is not None and type( v ) != str 
             else v for k, v in d.items() }
    
    prec        = int( max( 0, roundto ))
    keys        = list( d.keys()); keys.sort()
    ch_width    = 0 if title is None else 1 + len( title )
    str_frmt_c1 = '{}' if title is None else '{:<' + str( ch_width ) + '}'
    ch_width    = 2 + prec + max(  [ len( k ) for k in keys ]
                                 + [ 1 + math.ceil( math.log10( math.fabs( v )))
                                        for v in d.values() 
                                        if v is not None and type( v ) != str and v != 0 ] )
    
    str_frmt    = '{:>' + str( int( ch_width )) + '}'

    if roundto == 0:
        num_frmt    = '{:> ' + str( int( ch_width )) + ',d}'
    else:
        prec        = str( prec )
        num_frmt    = '{:> ' + str( int( ch_width )) + ',.' + prec + 'f}'    
    
    blank    = str_frmt.format( '' )
    line1    = [] if title is None else [ str_frmt_c1.format( '' ) ]
    line1   += [ str_frmt.format( k ) for k in keys ]
    line2    = [] if title is None else [ str_frmt_c1.format( title ) ]
    line2   += [ num_frmt.format( d[ k ] ) if not d[ k ] is None and type( d[ k ]) != str
                else blank for k in keys ]
    
    if linebreak_before:
        print( '' )
    print( ''.join( line1 ))
    print( ''.join( line2 ))
    if linebreak_after:
        print( '' )
        

def print_dict_of_dicts(    arg,
                            multiple            = 1, 
                            roundto             = 0, 
                            title               = None, 
                            linebreak_before    = True,
                            linebreak_after     = False,
                            bignum              = 1e6 ):
    
    for i in arg.keys():
        for j in arg[ i ].keys():
            x = arg[ i ][ j ]
            if not x is None and type( x ) != str and math.fabs( x ) >= bignum:
                a   = math.fabs( x )
                sgn = np.sign( x )
                e   = int( math.log10( a ))
                b   = round( a / 10.0 ** e, 2 )
                
                arg[ i ][ j ] = str( b ) + 'e' + str( e )
    
    if roundto != 0:
        d = {
            i: {
                j: round( multiple * x, roundto ) if not x is None and type( x ) != str
                else x for j, x in row.items()
            } for i, row in arg.items()
        }
    else:
        d = {
            i: {
                j: int( round( multiple * x )) if not x is None and type( x ) != str
                else x for j, x in row.items()
            } for i, row in arg.items()
        }

    prec        = int( max( 0, roundto ))
    row_labels  = list( d.keys()); row_labels.sort()
    col_labels  = []
    all_values  = []
    
    for k, v in d.items():
        col_labels += v.keys()
        all_values += v.values()
    
    col_labels  = list( set( col_labels )); col_labels.sort()
    all_labels  = row_labels + col_labels
    ch_width    = max( [ 0 if title is None else len( title ) ]
                     + [ len( k ) for k in row_labels ] ) + 1
    str_frmt_c1 = '{:<' + str( int( ch_width )) + '}'    
    ch_width    = 3 + prec + max( [ len( k ) for k in col_labels ]
                                + [ 1 + math.fabs(math.floor((math.log10(math.fabs( x )))))
                                    for x in all_values 
                                    if not x is None and type( x ) != str and x != 0 ]
                                + [ len( x ) for x in all_values if type( x ) == str ] )
    
    str_frmt    = '{:>' + str( int( ch_width )) + '}'
    
    if roundto == 0:
        num_frmt    = '{:> ' + str( int( ch_width )) + ',d}'
    else:
        prec        = str( prec )
        num_frmt    = '{:> ' + str( int( ch_width )) + ',.' + prec + 'f}'
        
    if linebreak_before:
        print( '' )
        
    line    = [ str_frmt_c1.format( '' if title is None else title ) ]
    line   += [ str_frmt.format( k ) for k in col_labels ]
        
    print( ''.join( line ))
    
    blank = str_frmt.format( '' )
    
    for r in row_labels:
        line        = [ str_frmt_c1.format( r ) ]
        row_vals    = d[ r ]
        for c in col_labels:
            if c in row_vals:
                x = row_vals[ c ]
                line.append( num_frmt.format( x ) if not x is None and type( x ) != str 
                            else str_frmt.format( x ) if type( x ) == str
                            else blank )
            else:
                line.append( str_frmt.format( '' ))
        print( ''.join( line ))
    
    if linebreak_after:
        print( '' )
        
    

def randbool( prob_true = 0.5 ):
    return random.random() <= prob_true
    
    
def sort_by_key( dictarg ):
    return OrderedDict( sorted( dictarg.items(), key = lambda t: t[ 0 ] ))

def ticksize_ceil(  x, tsz ):
    return round( tsz * math.ceil(  x / tsz ), int( math.ceil( -math.log10( tsz ))))

def ticksize_floor( x, tsz ):
    return round( tsz * math.floor( x / tsz ), int( math.ceil( -math.log10( tsz ))))

def ticksize_round( x, tsz ):
    return round( tsz * round( x / tsz ), int( math.ceil( -math.log10( tsz ))))

def unif():
    return 2.0 * random.random()


